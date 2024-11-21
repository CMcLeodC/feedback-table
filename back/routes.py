from flask import Flask, request, jsonify, send_from_directory
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from models import db, Contents, Dreamers, Users, Levels, Feedback, Dreamers_Users, Contents_Marketplace, Languages
from dotenv import load_dotenv
from sqlalchemy import text, func, and_
from sqlalchemy.orm import joinedload, aliased
import os

app = Flask(__name__)

load_dotenv()

app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URI')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

@app.route('/test_db', methods=['GET'])
def test_db():
    try:
        db.session.execute(text('SELECT 1'))
        return "Database connected successfully!", 200
    except Exception as e:
        return str(e), 500


@app.route('/contents', methods=['GET'])
def get_contents():
    contents = Contents.query.all()
    return jsonify([content.__repr__() for content in contents]), 200

@app.route('/contents/<int:id>', methods=['GET'])
def get_content_by_id(id):
    content = Contents.query.get_or_404(id)
    return jsonify(content.__repr__()), 200

@app.route('/contents', methods=['POST'])
def add_contents():
    data = request.json

    identifier_check = Contents.query.filter_by(identifier=data["identifier"]).first()
    if identifier_check:
        return jsonify("identifier already in use"), 400
    
    # first_available_id = db.session.query(func.max(Contents.id)).scalar()
    # new_contents_id = (first_available_id or 0) + 1

    new_contents = Contents(
        identifier=data["identifier"],
        type_id=data["type_id"],
        library_version_id=data["library_version_id"],
        active=data["active"],
        subfolder=data.get("subfolder", ""),
        supply=data.get("supply"),
        bundle_version=data.get("bundle_version"),
        repository=data.get("repository"),
        subcontentid=data.get("subcontentid"),
        synclink=data.get("synclink"),
        gdrive_folder=data.get("gdrive_folder"),
        smilies=data.get("smilies", 0),
        download_assets=data.get("download_assets", 0),
        textmeshpro=data.get("textmeshpro", 0),
        speech_recognition=data.get("speech_recognition", 0),
        progress=data.get("progress", 0),
        factoria_content_id=data.get("factoria_content_id")
    )
    db.session.add(new_contents)
    db.session.commit()

    return jsonify("Contents added"), 201

@app.route('/contents/<int:id>', methods=['DELETE'])
def delete_contents(id):
    content = Contents.query.get_or_404(id)

    db.session.delete(content)
    db.session.commit()

    return jsonify({"message": "Contents deleted", "id": content.id, "identifier": content.identifier}), 200

@app.route('/levels', methods=['GET'])
def get_levels():
    levels = Levels.query.all()
    return jsonify([level.__repr__() for level in levels]), 200

@app.route('/levels/<int:id>', methods=['GET'])
def get_level_by_id(id):
    level = Levels.query.get_or_404(id)
    return jsonify(level.__repr__()), 200

# @app.route('/levels', methods=['POST'])
# def add_level():
#     data = request.json
# Not necessary to add or delete levels

@app.route('/dreamers', methods=['GET'])
def get_dreamers():
    dreamers = Dreamers.query.limit(20).all()
    return jsonify([dreamer.__repr__() for dreamer in dreamers]), 200

@app.route('/dreamers/<int:id>', methods=['GET'])
def get_dreamer_by_id(id):
    dreamer = Dreamers.query.get_or_404(id)
    return jsonify(dreamer.__repr__()), 200

@app.route('/users', methods=['GET'])
def get_users():
    users = Users.query.limit(10).all()
    return jsonify([user.__repr__() for user in users]), 200

@app.route('/users/<int:id>', methods=['GET'])
def get_user_by_id(id):
    user = Users.query.get_or_404(id)
    return jsonify(user.__repr__()), 200

@app.route('/dreamers_users', methods=['GET'])
def get_dreamers_users():
    dreamers_users = Dreamers_Users.query.limit(30).all()
    return jsonify([dreamer_user.__repr__() for dreamer_user in dreamers_users]), 200

@app.route('/languages', methods=['GET'])
def get_langauges():
    languages = Languages.query.all()
    return jsonify([language.__repr__() for language in languages]), 200

@app.route('/dreamers_users/<int:user_id>', methods=['GET'])
def get_dreamers_by_user_id(user_id):
    dreamers_users = Dreamers_Users.query.filter_by(user_id=user_id).all()
    if not dreamers_users:
        return jsonify({"message": "No dreamers found for this user"}), 404
    dreamer_ids = [dreamer_user.dreamer_id for dreamer_user in dreamers_users]
    return jsonify(dreamer_ids), 200


# @app.route('/feedback', methods=['GET'])
# def get_feedback():
#     feedbacks = Feedback.query.limit(30).all()
#     return jsonify([feedback.serialize() for feedback in feedbacks]), 200

@app.route('/feedback', methods=['GET'])
def get_feedback():
    filter_value = request.args.get('filter', '')
    sort_field = request.args.get('sort', 'user_name')
    desc = request.args.get('desc', 'false').lower() == 'true'
    page = int(request.args.get('page', 1))
    per_page = int(request.args.get('per_page', 30))

    # title_subq = db.session.query(Contents_Marketplace.content_id, Contents_Marketplace.lang_id).filter(Contents_Marketplace.key == 'description').subquery()
    # title_stmt = db.select([Feedback]).where(Feedback.content_id == title_subq.c.content_id,
    #             Feedback.lang_id == title_subq.c.lang_id)
    # result = db.session.execute(title_stmt)

    title_subquery = db.session.query(Contents_Marketplace.value).filter(
        and_(
            Feedback.content_id == Contents_Marketplace.content_id,
            Feedback.lang_id == Contents_Marketplace.lang_id,
            Contents_Marketplace.key == 'title'
        )
    ).correlate(Feedback).scalar_subquery()

    description_subquery = db.session.query(Contents_Marketplace.value).filter(
        and_(
            Feedback.content_id == Contents_Marketplace.content_id,
            Feedback.lang_id == Contents_Marketplace.lang_id,
            Contents_Marketplace.key == 'description'
        )
    ).correlate(Feedback).scalar_subquery()

    keywords_subquery = db.session.query(Contents_Marketplace.value).filter(
        and_(
            Feedback.content_id == Contents_Marketplace.content_id,
            Feedback.lang_id == Contents_Marketplace.lang_id,
            Contents_Marketplace.key == 'keywords'
        )
    ).correlate(Feedback).scalar_subquery()

    sortable_fields = {
        'created_at': Feedback.created_at,
        'duration': Feedback.duration,
        'score': Feedback.score,
        'user_name': Users.name,
        'dreamer_name': Dreamers.name,
        'content_title': Contents_Marketplace.value,
        'level_name': Levels.name
    }

    query = db.session.query(
        Feedback.id,
        Feedback.user_id,
        Users.name.label("user_name"),
        Feedback.dreamer_id,
        Dreamers.name.label("dreamer_name"),
        Dreamers.avatar.label("dreamer_avatar"),
        Feedback.content_id,
        Contents.identifier.label("content_identifier"),
        title_subquery.label("content_title"),
        description_subquery.label("content_description"),
        keywords_subquery.label("content_keywords"),
        Feedback.library_version_id,
        Languages.local_name.label("lang_local_name"),
        Feedback.lang_id,
        Feedback.type_id,
        Feedback.game_mode_id,
        Feedback.reading_mode_id,
        Feedback.quiz_mode_id,
        Feedback.completed,
        Feedback.level_id,
        Levels.name.label("level_name"),
        Feedback.category_id,
        Feedback.subcategory_id,
        Feedback.stage_id,
        Feedback.duration,
        Feedback.total_score,
        Feedback.score,
        Feedback.failures,
        Feedback.details,
        Feedback.session_id,
        Feedback.game_id,
        Feedback.created_at,
        Feedback.updated_at
    ).join(Dreamers, Feedback.dreamer_id == Dreamers.id)\
    .join(Users, Feedback.user_id == Users.id)\
    .join(Contents, Feedback.content_id == Contents.id)\
    .join(Levels, Feedback.level_id == Levels.id)\
    .join(Languages, Feedback.lang_id == Languages.id)\
    .join(Contents_Marketplace,
          and_(Feedback.content_id == Contents_Marketplace.content_id,
               Feedback.lang_id == Contents_Marketplace.lang_id))

        
    
    if filter_value:
        filter_pattern = f"{filter_value}%"
        query = query.filter(
            (Users.name.like(filter_pattern)) |
            (Dreamers.name.like(filter_pattern))
        )

    if sort_field in sortable_fields:
        sort_column = sortable_fields[sort_field]
        query = query.order_by(sort_column.desc() if desc else sort_column.asc())
    
    # print("Query:", str(query))

    total_items = query.count()
    feedbacks = query.offset((page - 1) * per_page).limit(per_page).all()
 
    result = [{
        'id': feedback.id,
        'user_id': feedback.user_id,
        'user_name': feedback.user_name,
        'dreamer_id': feedback.dreamer_id,
        'dreamer_name': feedback.dreamer_name,
        'dreamer_avatar': feedback.dreamer_avatar,
        'content_id': feedback.content_id,
        'content_identifier': feedback.content_identifier,
        'content_title': feedback.content_title.strip('"') if feedback.content_title else None,
        'content_description': feedback.content_description.strip('"') if feedback.content_description else None,
        'content_keywords': feedback.content_keywords.strip('"') if feedback.content_keywords else None,
        'library_version_id': feedback.library_version_id,
        'lang_local_name': feedback.lang_local_name,
        'lang_id': feedback.lang_id,
        'type_id': feedback.type_id,
        'game_mode_id': feedback.game_mode_id,
        'reading_mode_id': feedback.reading_mode_id,
        'quiz_mode_id': feedback.quiz_mode_id,
        'completed': feedback.completed,
        'level_id': feedback.level_id,
        'level_name': feedback.level_name,
        'category_id': feedback.category_id,
        'subcategory_id': feedback.subcategory_id,
        'stage_id': feedback.stage_id,
        'duration': feedback.duration,
        'total_score': feedback.total_score,
        'score': feedback.score,
        'failures': feedback.failures,
        'details': feedback.details,
        'session_id': feedback.session_id,
        'game_id': feedback.game_id,
        'created_at': feedback.created_at.strftime('%d/%m/%y %H:%M:%S') if feedback.created_at else None,
        'updated_at': feedback.updated_at.strftime('%d/%m/%y %H:%M:%S') if feedback.updated_at else None,
    } for feedback in feedbacks]


    # print(result)
    # print('page and per_page: ', page, per_page)

    return jsonify({
        'data': result,
        'total': total_items
    }), 200


@app.route('/feedback', methods=['POST'])
def add_feedback():
    data = request.json
    
    if "user_id" not in data or "dreamer_id" not in data or "content_id" not in data:
        return jsonify({"error": "user_id, dreamer_id, and content_id are required fields"}), 400

    if "lang_id" in data and not (1 <= data["lang_id"] <= 8):
        return jsonify({"error": "Invalid lang_id, it must be between 1 and 8"}), 400

    if "level_id" in data and not (1 <= data["level_id"] <= 4):
        return jsonify({"error": "Invalid level_id, it must be between 1 and 4"}), 400
    
    # feedback_check = Feedback.query.filter_by(user_id=data["user_id"], dreamer_id=data["dreamer_id"], content_id=data["content_id"]).first()
    # if feedback_check:
    #     return jsonify({"error": "Feedback for this user, dreamer, and content already exists"}), 400

    new_feedback = Feedback(
        user_id=data["user_id"],
        dreamer_id=data["dreamer_id"],
        content_id=data["content_id"],
        library_version_id=data.get("library_version_id"),
        lang_id=data.get("lang_id"),
        type_id=data.get("type_id"),
        game_mode_id=data.get("game_mode_id"),
        reading_mode_id=data.get("reading_mode_id"),
        quiz_mode_id=data.get("quiz_mode_id"),
        completed=data.get("completed", False),
        level_id=data.get("level_id"),
        category_id=data.get("category_id"),
        subcategory_id=data.get("subcategory_id"),
        stage_id=data.get("stage_id"),
        duration=data.get("duration", 0.0),
        total_score=data.get("total_score", 0),
        score=data.get("score", 0.0),
        failures=data.get("failures", 0),
        details=data.get("details", ""),
        session_id=data.get("session_id"),
        game_id=data.get("game_id"),
        created_at=data.get("created_at"),
        updated_at=data.get("updated_at")
    )
    db.session.add(new_feedback)
    db.session.commit()

    return jsonify("Feedback added"), 201

@app.route('/feedback/<int:id>', methods=['DELETE'])
def delete_feedback(id):

    feedback_to_delete = Feedback.query.get_or_404(id)

    db.session.delete(feedback_to_delete)
    db.session.commit()

    return jsonify({"message": "Feedback Deleted", "ID": feedback_to_delete.id})

@app.route('/feedback/<int:id>', methods=['GET'])
def get_specific_feedback(id):
    ContentMarketplaceAlias = aliased(Contents_Marketplace)

    feedback = db.session.query(Feedback, Dreamers, Users, Contents, Levels, ContentMarketplaceAlias, Languages) \
        .join(Dreamers, Feedback.dreamer_id == Dreamers.id) \
        .join(Users, Feedback.user_id == Users.id) \
        .join(Contents, Feedback.content_id == Contents.id) \
        .join(Levels, Feedback.level_id == Levels.id) \
        .join(Languages, Feedback.lang_id == Languages.id) \
        .join(ContentMarketplaceAlias,
              and_(Feedback.content_id == ContentMarketplaceAlias.content_id,
                   Feedback.lang_id == ContentMarketplaceAlias.lang_id)) \
        .filter(ContentMarketplaceAlias.key == 'title', Feedback.id == id) \
        .first()

    if not feedback:
        return jsonify({"error": "Feedback not found"}), 404

    feedback, dreamer, user, content, level, content_marketplace, language = feedback

    return jsonify({
        'id': feedback.id,
        'user_id': feedback.user_id,
        'user_name': user.name if user else None,
        'dreamer_id': feedback.dreamer_id,
        'dreamer_name': dreamer.name if dreamer else None,
        'dreamer_avatar': dreamer.avatar if dreamer else None,
        'content_id': feedback.content_id,
        'content_identifier': content.identifier if content else None,
        'content_title': content_marketplace.value.strip('"') if content_marketplace else None,
        'content_data': [content.value.strip('"') for content in feedback.content_data] if feedback.content_data else None,
        'library_version_id': feedback.library_version_id,
        'lang_local_name': language.local_name if language else None,
        'lang_id': feedback.lang_id,
        'type_id': feedback.type_id,
        'game_mode_id': feedback.game_mode_id,
        'reading_mode_id': feedback.reading_mode_id,
        'quiz_mode_id': feedback.quiz_mode_id,
        'completed': feedback.completed,
        'level_id': feedback.level_id,
        'level_name': level.name if level else None,
        'category_id': feedback.category_id,
        'subcategory_id': feedback.subcategory_id,
        'stage_id': feedback.stage_id,
        'duration': feedback.duration,
        'total_score': feedback.total_score,
        'score': feedback.score,
        'failures': feedback.failures,
        'details': feedback.details,
        'session_id': feedback.session_id,
        'game_id': feedback.game_id,
        'created_at': feedback.created_at.strftime('%d/%m/%y %H:%M:%S') if feedback.created_at else None,
        'updated_at': feedback.updated_at.strftime('%d/%m/%y %H:%M:%S') if feedback.updated_at else None,
    }), 200

@app.route('/back/images/dreamer_avatars/<filename>', methods=['GET'])
def get_dreamer_avatar(filename):
    avatar_directory = 'images/dreamer_avatars'  # relative path from back/routes.py
    filepath = os.path.join(avatar_directory, filename)
    
    # Check if the file exists and serve it, or return the default image if missing
    if os.path.exists(filepath):
        return send_from_directory(avatar_directory, filename)
    else:
        return send_from_directory(avatar_directory, 'default.png')

if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Creates tables based on models if they don't exist yet
    app.run(debug=True)
