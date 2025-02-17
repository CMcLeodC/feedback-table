from flask import Flask, request, jsonify, send_from_directory
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from models import db, Contents, Dreamers, Users, Levels, Feedback, Dreamers_Users, Contents_Marketplace, Languages, ContentsArts, ContentsFeedbackCategories, Feedback_Types, ContentsFeedbackSubcategories
from dotenv import load_dotenv
from sqlalchemy import text, func, and_, or_, event
import time
from sqlalchemy.orm import joinedload, aliased
import os
import logging

app = Flask(__name__)

load_dotenv()

app.debug = True
app.logger.setLevel(logging.INFO)

app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URI')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

print(app.url_map)

@app.route('/contents', methods=['GET'])
def get_contents():
    contents = Contents.query.all()
    return jsonify([content.__repr__() for content in contents]), 200



@app.route('/contents/<int:id>', methods=['GET'])
def get_content_by_id(id):
    content = Contents.query.get_or_404(id)
    return jsonify(content.__repr__()), 200

@app.route('/contents_arts', methods=['GET'])
def get_contents_arts():
    arts = ContentsArts.query.all()
    return jsonify([{
        'content_id': art.content_id,
        'icon_url': art.icon_url,
        'thumbnail_url': art.thumbnail_url,
        'created_at': art.created_at,
        'updated_at': art.updated_at
    } for art in arts]), 200

@app.route('/contents_arts/<int:content_id>', methods=['GET'])
def get_content_art_by_id(content_id):
    art = ContentsArts.query.get_or_404(content_id)
    return jsonify({
        'content_id': art.content_id,
        'icon_url': art.icon_url,
        'thumbnail_url': art.thumbnail_url,
        'created_at': art.created_at,
        'updated_at': art.updated_at
    }), 200

@app.route('/contents_feedback_categories', methods=['GET'])
def get_contents_feedbacks_categories():
    categories = ContentsFeedbackCategories.query.all()
    return jsonify([{
        'content_id': category.content_id,
        'category_id': category.category_id,
        'name': category.name,
        'created_at': category.created_at,
        'updated_at': category.updated_at
    } for category in categories]), 200

@app.route('/contents_feedback_categories/<int:content_id>/<int:category_id>', methods=['GET'])
def get_content_feedback_category_by_id(content_id, category_id):
    category = ContentsFeedbackCategories.query.filter_by(content_id=content_id, category_id=category_id).first()
    
    if not category:
        return jsonify({"error": "Category not found"}), 404
    
    return jsonify({
        'content_id': category.content_id,
        'category_id': category.category_id,
        'name': category.name,
        'created_at': category.created_at,
        'updated_at': category.updated_at
    }), 200

@app.route('/contents_feedback_subcategories', methods=['GET'])
def get_contents_feedbacks_subcategories():
    subcategories = ContentsFeedbackSubcategories.query.all()
    return jsonify([{
        'content_id': subcategory.content_id,
        'subcategory_id': subcategory.subcategory_id,
        'name': subcategory.name,
        'created_at': subcategory.created_at,
        'updated_at': subcategory.updated_at
    } for subcategory in subcategories]), 200

@app.route('/levels', methods=['GET'])
def get_levels():
    levels = Levels.query.all()
    return jsonify([level.__repr__() for level in levels]), 200

@app.route('/levels/<int:id>', methods=['GET'])
def get_level_by_id(id):
    level = Levels.query.get_or_404(id)
    return jsonify(level.__repr__()), 200

@app.route('/dreamers', methods=['GET'])
def get_dreamers():
    dreamers = Dreamers.query.limit(20).all()
    return jsonify([dreamer.__repr__() for dreamer in dreamers]), 200

@app.route('/dreamers/<int:id>', methods=['GET'])
def get_dreamer_by_id(id):
    dreamer = Dreamers.query.get_or_404(id)
    return jsonify({
    "age": dreamer.age,
    "avatar": dreamer.avatar,
    "birthdate": dreamer.birthdate,
    "coins": dreamer.coins,
    "created_at": dreamer.created_at,
    "deleted_at": dreamer.deleted_at,
    "details": dreamer.details,
    "game_mode": dreamer.game_mode,
    "game_reading_level": dreamer.game_reading_level,
    "gems": dreamer.gems,
    "id": dreamer.id,
    "local_flag": dreamer.local_flag,
    "name": dreamer.name,
    "password": dreamer.password,
    "pending_delete": dreamer.pending_delete,
    "registration_number": dreamer.registration_number,
    "tale_font_type": dreamer.tale_font_type,
    "tale_reading_level": dreamer.tale_reading_level,
    "tale_reading_mode": dreamer.tale_reading_mode,
    "tutorial_completed": dreamer.tutorial_completed,
    "updated_at": dreamer.updated_at,
    "visual_mode": dreamer.visual_mode
}
), 200

@app.route('/users', methods=['GET'])
def get_users():
    users = Users.query.limit(10).all()
    return jsonify([user.__repr__() for user in users]), 200

@app.route('/users/<int:id>', methods=['GET'])
def get_user_by_id(id):
    user = Users.query.get_or_404(id)
    return jsonify({
        "id": user.id,
        # "name": user.name,
        "username": user.username,
        # "email": user.email,
        # "is_college": user.is_college,
        # "allowed_access_la": user.allowed_access_la,
        # "validated": user.validated,
        # "teacher_college": user.teacher_college,
        # "is_third_party": user.is_third_party,
        # "max_children": user.max_children,
        # "max_devices": user.max_devices,
        # "details": user.details,
        # "welcomed": user.welcomed,
        # "privacy_accepted": user.privacy_accepted,
        # "lang_id": user.lang_id,
        # "emailing": user.emailing,
        # "zero_emailing": user.zero_emailing,
        # "email1": user.email1,
        # "library_version_id": user.library_version_id,
        # "last_remindered": user.last_remindered,
        # "braintree_id": user.braintree_id,
        # "paypal_email": user.paypal_email,
        # "card_brand": user.card_brand,
        # "card_last_four": user.card_last_four,
        # "trial_ends_at": user.trial_ends_at,
        # "braintree_subscription_id": user.braintree_subscription_id,
        # "web": user.web,
        # "stripe_id": user.stripe_id,
        # "pm_type": user.pm_type,
        # "pm_last_four": user.pm_last_four,
        # "has_child_creation_password": user.has_child_creation_password,
        # "pending_unsubscribe": user.pending_unsubscribe,
        # "pending_delete": user.pending_delete,
        # "sso": user.sso,
        # "sso_provider": user.sso_provider,
        # "sso_provider_uuid": user.sso_provider_uuid,
        # "password": user.password,
        # "remember_token": user.remember_token,
        # "role_id": user.role_id,
        # "created_at": user.created_at,
        # "updated_at": user.updated_at,
        # "deleted_at": user.deleted_at
    }), 200


@app.route('/dreamer_user', methods=['GET'])
def get_dreamers_users():
    dreamers_users = Dreamers_Users.query.limit(30).all()
    return jsonify([dreamer_user.__repr__() for dreamer_user in dreamers_users]), 200

@app.route('/languages', methods=['GET'])
def get_langauges():
    languages = Languages.query.all()
    return jsonify([language.__repr__() for language in languages]), 200

@app.route('/feedback_types', methods=['GET'])
def get_feedback_types():
    types = Feedback_Types.query.all()
    return jsonify([type.__repr__() for type in types]), 200



@app.route('/feedback', methods=['GET'])
def feedback():
    filter_value = request.args.get('filter', '')
    sort_field = request.args.get('sort', 'created_at')
    desc = request.args.get('desc', 'false').lower() == 'true'
    page = int(request.args.get('page', 1))
    per_page = int(request.args.get('per_page', 30))

    app.logger.info(f"Request Params - Filter: {filter_value}, Sort: {sort_field}, Desc: {desc}, Page: {page}, Per Page: {per_page}")


    query = db.session.query(
        Feedback.id,
        Feedback.created_at,
        Feedback.duration,
        Feedback.score,
        Feedback.user_id,
        Users.username.label("user_name"),
        Feedback.dreamer_id,
        Dreamers.name.label("dreamer_name"),
        Dreamers.avatar.label("dreamer_avatar"),
        Feedback.level_id,
        Feedback.total_score,
        Feedback.score,
        Feedback.failures,
        Feedback.content_id,
        Feedback.lang_id
    ).join(Dreamers, Feedback.dreamer_id == Dreamers.id) \
    .join(Users, Feedback.user_id == Users.id)

    if filter_value:
        filter_pattern = f"%{filter_value}%"
        query = query.filter(func.lower(Users.username).like(func.lower(filter_pattern)))
        app.logger.info(f"Applied Filter - Filter Pattern: {filter_pattern}")

    # query = query.order_by(Feedback.created_at).limit(30)

    sortable_fields = {
        'created_at': Feedback.created_at,
        'id': Feedback.id,
        'duration': Feedback.duration,
        'score': Feedback.score,
        'user_name': Users.username,
        'dreamer_name': Dreamers.name,
        'level_name': Levels.name
    }

    if sort_field in sortable_fields:
        sort_column = sortable_fields[sort_field]
        query = query.order_by(sort_column.desc() if desc else sort_column.asc())
        app.logger.info(f"Applied Sorting - Field: {sort_field}, Desc: {desc}")
    
    offset = (page - 1) * per_page
    query = query.offset(offset).limit(per_page) 

    feedbacks = query.limit(per_page).all()
    app.logger.info(f"Feedback Query Results: {feedbacks}")

    content_lang_pairs = [(fb.content_id, fb.lang_id) for fb in feedbacks]
    titles = db.session.query(
        Contents_Marketplace.content_id,
        Contents_Marketplace.lang_id,
        Contents_Marketplace.value
    ).filter(
        Contents_Marketplace.key == 'title',
        and_(
            Contents_Marketplace.content_id.in_([pair[0] for pair in content_lang_pairs]),
            Contents_Marketplace.lang_id.in_([pair[1] for pair in content_lang_pairs])
        )
    ).all()

    title_map = {(t.content_id, t.lang_id): t.value for t in titles}

    user_ids = [fb.user_id for fb in feedbacks]
    dreamer_ids = [fb.dreamer_id for fb in feedbacks]

    users = db.session.query(Users).filter(Users.id.in_(user_ids)).all()
    dreamers = db.session.query(Dreamers).filter(Dreamers.id.in_(dreamer_ids)).all()

    user_map = {user.id: user.username for user in users}
    dreamer_map = {dreamer.id: dreamer.name for dreamer in dreamers}
    level_map = {
        1: 'Apprentice',
        2: 'Intermediate',
        3: 'Advanced',
        4: 'Master'
    }

    # total = db.session.query(Feedback.id).count()

    total_rows_query = text("""
        SELECT TABLE_ROWS 
        FROM information_schema.tables 
        WHERE TABLE_SCHEMA = :schema AND TABLE_NAME = :table
    """)
    result = db.session.execute(
        total_rows_query,
        {"schema": "feedback", "table": "feedback"}
    )
    total_rows = result.scalar()
    app.logger.info(f"Total Rows: {total_rows}")
   

    data = [{
        'id': feedback.id,
        'created_at': feedback.created_at,
        'duration': feedback.duration,
        'score': feedback.score,
        'user_id': feedback.user_id,
        'user_name': user_map.get(feedback.user_id, None),
        'dreamer_id': feedback.dreamer_id,
        'dreamer_name': dreamer_map.get(feedback.dreamer_id, None),
        'dreamer_avatar': feedback.dreamer_avatar,
        'level_id': feedback.level_id,
        'level_name': level_map.get(feedback.level_id, None),
        'total_score': feedback.total_score,
        'content_title': title_map.get((feedback.content_id, feedback.lang_id), None)
    } for feedback in feedbacks]
    app.logger.info(f"Response Data: {data}")
    
    return jsonify ({
        'data': data,
        'total': total_rows
    }), 200



@app.route('/feedback/<int:id>', methods=['GET'])
def get_specific_feedback(id):
    # Creating an alias for Contents_Marketplace
    ContentMarketplaceAlias = aliased(Contents_Marketplace)

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

    feedback_data = db.session.query(
    Feedback, Dreamers, Users, Contents, Levels, ContentMarketplaceAlias, Languages, Feedback_Types, ContentsFeedbackCategories, ContentsFeedbackSubcategories,
    title_subquery.label('content_title'),
    description_subquery.label('content_description'),
    keywords_subquery.label('content_keywords'),
    ContentsFeedbackCategories.name.label("category_name"),
    ContentsFeedbackSubcategories.name.label("subcategory_name")
) \
    .join(Dreamers, Feedback.dreamer_id == Dreamers.id) \
    .join(Users, Feedback.user_id == Users.id) \
    .join(Contents, Feedback.content_id == Contents.id) \
    .join(Levels, Feedback.level_id == Levels.id) \
    .join(Languages, Feedback.lang_id == Languages.id) \
    .join(Feedback_Types, Feedback.type_id == Feedback_Types.id) \
    .join(ContentMarketplaceAlias,
          and_(Feedback.content_id == ContentMarketplaceAlias.content_id,
               Feedback.lang_id == ContentMarketplaceAlias.lang_id)) \
    .join(ContentsFeedbackCategories,
          and_(
            Feedback.content_id == ContentsFeedbackCategories.content_id,
            Feedback.category_id == ContentsFeedbackCategories.category_id
            ), isouter=True)\
    .join(ContentsFeedbackSubcategories,
          and_(
            Feedback.content_id == ContentsFeedbackSubcategories.content_id,
            Feedback.subcategory_id == ContentsFeedbackSubcategories.subcategory_id
          ), isouter=True)\
    .filter(Feedback.id == id) \
    .first()

    if not feedback_data:
        return jsonify({"error": "Feedback not found"}), 404

    # Unpack the results into the appropriate variables
    feedback, dreamer, user, content, level, content_marketplace, language, feedback_type, contents_feedback_categories, contents_feedback_subcategories, content_title, content_description, content_keywords, category_name, subcategory_name = feedback_data

    return jsonify({
        'id': feedback.id,
        'user_id': feedback.user_id,
        'user_name': user.name if user else None,
        'dreamer_id': feedback.dreamer_id,
        'dreamer_name': dreamer.name if dreamer else None,
        'dreamer_avatar': dreamer.avatar if dreamer else None,
        'content_id': feedback.content_id,
        'content_identifier': content.identifier if content else None,
        'content_title': content_title.strip('"') if content_title else None,
        'content_description': content_description.strip('"') if content_description else None,
        'content_keywords': content_keywords.strip('"') if content_keywords else None,
        'library_version_id': feedback.library_version_id,
        'lang_local_name': language.local_name if language else None,
        'lang_id': feedback.lang_id,
        'type_name': feedback_type.feedback_type if feedback_type else None,
        'type_id': feedback.type_id,
        'game_mode_id': feedback.game_mode_id,
        'reading_mode_id': feedback.reading_mode_id,
        'quiz_mode_id': feedback.quiz_mode_id,
        'completed': feedback.completed,
        'level_id': feedback.level_id,
        'level_name': level.name if level else None,
        'category_name': category_name if category_name else None,
        'category_id': feedback.category_id,
        'subcategory_name': subcategory_name if subcategory_name else None,
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


def _build_feedback_query(filter_value='', sort_field='user_name', desc=False, page=1, per_page=30):
    """
    Builds a dynamic query for fetching Feedback data with filtering,
    sorting, and pagination.
    """
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
            Feedback_Types.feedback_type.label("type_name"),
            Feedback.type_id,
            Feedback.game_mode_id,
            Feedback.reading_mode_id,
            Feedback.quiz_mode_id,
            Feedback.completed,
            Feedback.level_id,
            Levels.name.label("level_name"),
            ContentsFeedbackCategories.name.label("category_name"),
            Feedback.category_id,
            ContentsFeedbackSubcategories.name.label("subcategory_name"),
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
        .join(Feedback_Types, Feedback.type_id == Feedback_Types.id)\
        .join(ContentsFeedbackCategories,
            and_(
                Feedback.content_id == ContentsFeedbackCategories.content_id,
                Feedback.category_id == ContentsFeedbackCategories.category_id
                ), isouter=True)\
        .join(ContentsFeedbackSubcategories,
            and_(
                Feedback.content_id == ContentsFeedbackSubcategories.content_id,
                Feedback.subcategory_id == ContentsFeedbackSubcategories.subcategory_id
            ), isouter=True)

    if filter_value:
            filter_pattern = f"%{filter_value}%"
            query = query.filter(
                (Users.name.ilike(filter_pattern)) |
                (Dreamers.name.ilike(filter_pattern)) |
                (title_subquery.ilike(filter_pattern))
            )

    sortable_fields = {
            'created_at': Feedback.created_at,
            'duration': Feedback.duration,
            'score': Feedback.score,
            'user_name': Users.name,
            'dreamer_name': Dreamers.name,
            'content_title': title_subquery,
            'level_name': Levels.name
        }

    return query


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
        @event.listens_for(db.engine, "before_cursor_execute")
        def before_cursor_execute(conn, cursor, statement, parameters, context, executemany):
            context._query_start_time = time.time()

        @event.listens_for(db.engine, "after_cursor_execute")
        def after_cursor_execute(conn, cursor, statement, parameters, context, executemany):
            total_time = time.time() - context._query_start_time
            print(f"Query: {statement} executed in {total_time:.5f} seconds")
        db.create_all()
    app.run(debug=True)
