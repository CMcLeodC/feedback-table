from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from models import db, Contents, Dreamers, Users, Levels, Feedback, Dreamers_Users, Contents_Marketplace
from dotenv import load_dotenv
from sqlalchemy import text, func, and_
from sqlalchemy.orm import joinedload
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

    sortable_fields = {
        'created_at': Feedback.created_at,
        'duration': Feedback.duration,
        'total_score': Feedback.total_score,
        'user_name': Users.name,
        'dreamer_name': Dreamers.name,
        'content_title': Contents_Marketplace.value,
        'level_name': Levels.name
    }

    query = db.session.query(Feedback, Dreamers, Users, Contents, Levels, Contents_Marketplace)\
        .join(Dreamers, Feedback.dreamer_id == Dreamers.id)\
        .join(Users, Feedback.user_id == Users.id)\
        .join(Contents, Feedback.content_id == Contents.id)\
        .join(Levels, Feedback.level_id == Levels.id)\
        .join(Contents_Marketplace,
              and_(Feedback.content_id == Contents_Marketplace.content_id,
                   Feedback.lang_id == Contents_Marketplace.lang_id)) \
        .filter(Contents_Marketplace.key == 'title')
    
    if filter_value:
        filter_pattern = f"%{filter_value}%"
        query = query.filter(
            (Users.name.ilike(filter_pattern)) |
            (Dreamers.name.ilike(filter_pattern)) |
            (Contents.identifier.ilike(filter_pattern))
        )

    # if sort_field == 'dateDesc':
    #     query = query.order_by(Feedback.created_at.desc())
    # elif sort_field == 'dateAsc':
    #     query = query.order_by(Feedback.duration.asc())
    # elif sort_field == 'duration':
    #     query = query.order_by(Feedback.duration.desc())
    # elif sort_field == 'score':
    #     query = query.order_by(Feedback.total_score.desc()) 

    if sort_field in sortable_fields:
        sort_column = sortable_fields[sort_field]
        if desc:
            query = query.order_by(sort_column.desc())
        else:
            query = query.order_by(sort_column.asc())

    feedbacks = query.limit(30).all()
 
    return jsonify([{
        'id': feedback.id,
        'user_id': feedback.user_id,
        'user_name': user.name,
        'dreamer_id': feedback.dreamer_id,
        'dreamer_name': dreamer.name,
        'dreamer_avatar': dreamer.avatar,
        'content_id': feedback.content_id,
        'content_identifier': content.identifier,
        'content_title': content_marketplace.value,
        'library_version_id': feedback.library_version_id,
        'lang_id': feedback.lang_id,
        'type_id': feedback.type_id,
        'game_mode_id': feedback.game_mode_id,
        'reading_mode_id': feedback.reading_mode_id,
        'quiz_mode_id': feedback.quiz_mode_id,
        'completed': feedback.completed,
        'level_id': feedback.level_id,
        'level_name': level.name,
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
        'created_at': feedback.created_at.isoformat() if feedback.created_at else None,
        'updated_at': feedback.updated_at.isoformat() if feedback.updated_at else None,
    } for feedback, dreamer, user, content, level, content_marketplace in feedbacks]), 200


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
    feedback = Feedback.query.options(
        joinedload(Feedback.user),
        joinedload(Feedback.dreamer),
        joinedload(Feedback.content),
        joinedload(Feedback.level)
    ).get_or_404(id)

    return jsonify({
        'id': feedback.id,
        'user_id': feedback.user_id,
        'user_name': feedback.user.name if feedback.user else None,
        'dreamer_id': feedback.dreamer_id,
        'dreamer_name': feedback.dreamer.name if feedback.dreamer else None,
        'dreamer_avatar': feedback.dreamer.avatar if feedback.dreamer else None,
        'content_id': feedback.content_id,
        'content_identifier': feedback.content.identifier if feedback.content else None,
        'content_title': feedback.content_data.value if feedback.content_data else None,
        'library_version_id': feedback.library_version_id,
        'lang_id': feedback.lang_id,
        'type_id': feedback.type_id,
        'game_mode_id': feedback.game_mode_id,
        'reading_mode_id': feedback.reading_mode_id,
        'quiz_mode_id': feedback.quiz_mode_id,
        'completed': feedback.completed,
        'level_id': feedback.level_id,
        'level_name': feedback.level.name if feedback.level else None,
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
        'created_at': feedback.created_at.isoformat() if feedback.created_at else None,
        'updated_at': feedback.updated_at.isoformat() if feedback.updated_at else None,
    }), 200

if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Creates tables based on models if they don't exist yet
    app.run(debug=True)
