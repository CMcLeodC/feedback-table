from flask_sqlalchemy import SQLAlchemy
from datetime import datetime, timezone
from sqlalchemy import and_
from sqlalchemy.orm import foreign

db = SQLAlchemy()

class Contents(db.Model):
    __tablename__ = 'contents'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    identifier = db.Column(db.String(255)) 
    type_id = db.Column(db.Integer)
    library_version_id = db.Column(db.Integer)
    active = db.Column(db.Integer)
    subfolder = db.Column(db.String(255))
    supply = db.Column(db.String(255))
    bundle_version = db.Column(db.Integer)
    repository = db.Column(db.String(255))
    subcontentid = db.Column(db.String(255))
    synclink = db.Column(db.String(255))
    gdrive_folder = db.Column(db.String(255))
    smilies = db.Column(db.Integer)
    download_assets = db.Column(db.Integer)
    textmeshpro = db.Column(db.Integer)
    speech_recognition = db.Column(db.Integer)
    progress = db.Column(db.Integer)
    factoria_content_id = db.Column(db.Integer)
    created_at = db.Column(db.DateTime, default=datetime.now(timezone.utc))
    updated_at = db.Column(db.DateTime, default=datetime.now(timezone.utc), onupdate=datetime.now(timezone.utc))

    def __repr__(self):
        return f'<Contents id={self.id}, identifier={self.identifier}>'

class ContentsArts(db.Model):
    __tablename__ = 'contents_arts'

    content_id = db.Column(db.Integer, db.ForeignKey('contents.id'), primary_key=True)
    icon_url = db.Column(db.String(255))
    thumbnail_url = db.Column(db.String(255))
    created_at = db.Column(db.DateTime, default=datetime.now(timezone.utc))
    updated_at = db.Column(db.DateTime, default=datetime.now(timezone.utc), onupdate=datetime.now(timezone.utc))

    content = db.relationship('Contents', backref='arts')

    def __repr__(self):
        return f"<ContentsArts content_id={self.content_id}, icon_url={self.icon_url}, thumbnail_url={self.thumbnail_url}>"

class ContentsFeedbackCategories(db.Model):
    __tablename__ = 'contents_feedback_categories'

    content_id = db.Column(db.Integer, db.ForeignKey('contents.id'), primary_key=True) 
    category_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    created_at = db.Column(db.DateTime, default=datetime.now(timezone.utc))
    updated_at = db.Column(db.DateTime, default=datetime.now(timezone.utc), onupdate=datetime.now(timezone.utc))

    def __repr__(self):
        return f"<ContentsArts content_id={self.content_id}, category_id={self.category_id}, name={self.name}>"

class ContentsFeedbackSubcategories(db.Model):
    __tablename__ = 'contents_feedback_subcategories'

    content_id = db.Column(db.Integer, primary_key=True) 
    subcategory_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    created_at = db.Column(db.DateTime, default=datetime.now(timezone.utc))
    updated_at = db.Column(db.DateTime, default=datetime.now(timezone.utc), onupdate=datetime.now(timezone.utc))

    def __repr__(self):
        return f"<ContentsArts content_id={self.content_id}, category_id={self.category_id}, name={self.name}>"


class Levels(db.Model):
    __tablename__ = 'levels'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(255))
    min_age = db.Column(db.Integer)
    max_age = db.Column(db.Integer)
    requisites = db.Column(db.String(255))
    created_at = db.Column(db.DateTime, default=datetime.now(timezone.utc))
    updated_at = db.Column(db.DateTime, default=datetime.now(timezone.utc), onupdate=datetime.now(timezone.utc))

    def __repr__(self):
        return f'<Levels id={self.id}, name={self.name}>'
    
class Dreamers(db.Model):
    __tablename__ = 'dreamers'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    birthdate = db.Column(db.Date)
    age = db.Column(db.Integer)
    registration_number = db.Column(db.String(255))
    details = db.Column(db.Text)
    avatar = db.Column(db.String(255))
    coins = db.Column(db.Integer)
    gems = db.Column(db.Integer)
    local_flag = db.Column(db.String(255))
    game_mode = db.Column(db.String(255))
    game_reading_level = db.Column(db.Integer)
    tale_reading_level = db.Column(db.Integer)
    tale_reading_mode = db.Column(db.String(255))
    tale_font_type = db.Column(db.String(255))
    visual_mode = db.Column(db.String(255))
    tutorial_completed = db.Column(db.Integer)
    password = db.Column(db.String(255))
    pending_delete = db.Column(db.Integer)
    created_at = db.Column(db.DateTime, default=datetime.now(timezone.utc))
    updated_at = db.Column(db.DateTime, default=datetime.now(timezone.utc), onupdate=datetime.now(timezone.utc))
    deleted_at = db.Column(db.DateTime)

    def __repr__(self):
        return f'<Dreamers id={self.id}, name={self.name}>'

class Users(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    username = db.Column(db.String(255))
    email = db.Column(db.String(255))
    is_college = db.Column(db.Boolean)
    allowed_access_la = db.Column(db.Boolean)
    validated = db.Column(db.Boolean)
    teacher_college = db.Column(db.Boolean)
    is_third_party = db.Column(db.Boolean)
    max_children = db.Column(db.Integer)
    max_devices = db.Column(db.Integer)
    details = db.Column(db.Text)
    welcomed = db.Column(db.Boolean)
    # privacy_accepted = db.Column(db.Boolean)
    privacy_accepted = db.Column(db.DateTime)
    lang_id = db.Column(db.Integer)
    emailing = db.Column(db.Boolean)
    zero_emailing = db.Column(db.Boolean)
    email1 = db.Column(db.String(255))
    library_version_id = db.Column(db.Integer)
    last_remindered = db.Column(db.DateTime)
    braintree_id = db.Column(db.String(255))
    paypal_email = db.Column(db.String(255))
    card_brand = db.Column(db.String(255))
    card_last_four = db.Column(db.String(10))
    trial_ends_at = db.Column(db.DateTime)
    braintree_subscription_id = db.Column(db.String(255))
    web = db.Column(db.Boolean)
    stripe_id = db.Column(db.String(255))
    pm_type = db.Column(db.String(255))
    pm_last_four = db.Column(db.String(10))
    has_child_creation_password = db.Column(db.Boolean)
    pending_unsubscribe = db.Column(db.Boolean)
    pending_delete = db.Column(db.Boolean)
    # sso = db.Column(db.Boolean)
    sso = db.Column(db.String(255))
    sso_provider = db.Column(db.String(255))
    sso_provider_uuid = db.Column(db.String(255))
    password = db.Column(db.String(255))
    remember_token = db.Column(db.String(255))
    role_id = db.Column(db.Integer)
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())
    updated_at = db.Column(db.DateTime, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())
    deleted_at = db.Column(db.DateTime)

    def __repr__(self):
        return f"<User id={self.id}, username='{self.username}', email='{self.email}', role_id={self.role_id}, created_at={self.created_at}>"

class Dreamers_Users(db.Model):
    __tablename__ = 'dreamers_users'

    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), primary_key=True)
    dreamer_id = db.Column(db.Integer, db.ForeignKey('dreamers.id'), primary_key=True)
    rol = db.Column(db.String(10))
    link_in_process = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())
    updated_at = db.Column(db.DateTime, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())

    def __repr__(self):
        return f"<User id={self.user_id}, Dreamer id='{self.dreamer_id}'>"
    
class Contents_Marketplace(db.Model):
    __tablename__ = 'contents_marketplace'

    content_id = db.Column(db.Integer, primary_key=True) 
    lang_id = db.Column(db.Integer, primary_key=True) 
    key = db.Column(db.String(255), primary_key=True)
    value = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())
    updated_at = db.Column(db.DateTime, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())

    def __repr__(self):
        return f"<ContentsMarketplace content_id={self.content_id}, lang_id={self.lang_id}, key={self.key}>"

class Languages(db.Model):
    __tablename__ = 'languages'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(255))
    local_name = db.Column(db.String(255))
    i18n = db.Column(db.String(255))
    iso_code = db.Column(db.String(10))
    active = db.Column(db.Integer)
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())
    updated_at = db.Column(db.DateTime, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())

    def __repr__(self):
        return f'<Languages id={self.id}, name={self.name}>'


class Feedback_Types(db.Model):
    __tablename__ = 'feedback_types'

    id = db.Column(db.Integer, primary_key=True)
    feedback_type = db.Column(db.String(255))

    def __repr__(self):
        return f'<Languages id={self.id}, name={self.feedback_type}>'

class Feedback(db.Model):
    __tablename__ = 'feedback'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    dreamer_id = db.Column(db.Integer, db.ForeignKey('dreamers.id'))
    content_id = db.Column(db.Integer, db.ForeignKey('contents.id'))
    library_version_id = db.Column(db.Integer)
    lang_id = db.Column(db.Integer, db.ForeignKey('languages.id'))
    type_id = db.Column(db.Integer, db.ForeignKey('feedback_types.id'))
    game_mode_id = db.Column(db.Integer)
    reading_mode_id = db.Column(db.Integer)
    quiz_mode_id = db.Column(db.Integer)
    completed = db.Column(db.Boolean)
    level_id = db.Column(db.Integer, db.ForeignKey('levels.id'))
    category_id = db.Column(db.Integer)
    subcategory_id = db.Column(db.Integer)
    stage_id = db.Column(db.Integer)
    duration = db.Column(db.Float)
    total_score = db.Column(db.Integer)
    score = db.Column(db.Float)
    failures = db.Column(db.Integer)
    details = db.Column(db.Text)
    session_id = db.Column(db.Integer)
    game_id = db.Column(db.Integer)
    created_at = db.Column(db.DateTime)
    updated_at = db.Column(db.DateTime)

    user = db.relationship('Users', backref='feedbacks')
    dreamer = db.relationship('Dreamers', backref='feedbacks')
    content = db.relationship('Contents', backref='feedbacks')
    level = db.relationship('Levels', backref='feedbacks')
    language = db.relationship('Languages', backref='feedbacks')
    types = db.relationship('Feedback_Types', backref='feedbacks')

    content_data = db.relationship(
        'Contents_Marketplace',
        primaryjoin=and_(
            foreign(content_id) == Contents_Marketplace.content_id,
            foreign(lang_id) == Contents_Marketplace.lang_id
        ),
        viewonly=True,
        uselist=True
    )

    category_name = db.relationship(
        'ContentsFeedbackCategories',
        primaryjoin=and_(
            foreign(content_id) == ContentsFeedbackCategories.content_id,
            foreign(category_id) == ContentsFeedbackCategories.category_id
        ),
        viewonly=True
    )

    subcategory_name = db.relationship(
        'ContentsFeedbackSubcategories',
        primaryjoin=and_(
            foreign(content_id) == ContentsFeedbackSubcategories.content_id,
            foreign(subcategory_id) == ContentsFeedbackSubcategories.subcategory_id
        ),
        viewonly=True
    )

    def serialize(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'dreamer_id': self.dreamer_id,
            'content_id': self.content_id,
            'content_data': [
                {
                    'key': item.key,
                    'value': item.value,
                    'created_at': item.created_at.isoformat() if item.created_at else None,
                    'updated_at': item.updated_at.isoformat() if item.updated_at else None
                }
                for item in self.content_data
            ] if self.content_data else None,
            'library_version_id': self.library_version_id,
            'lang_id': self.lang_id,
            'type_id': self.type_id,
            'game_mode_id': self.game_mode_id,
            'reading_mode_id': self.reading_mode_id,
            'quiz_mode_id': self.quiz_mode_id,
            'completed': self.completed,
            'level_id': self.level_id,
            'category_name': self.category_name,
            'category_id': self.category_id,
            'subcategory_name': self.subcategory_name,
            'subcategory_id': self.subcategory_id,
            'stage_id': self.stage_id,
            'duration': self.duration,
            'total_score': self.total_score,
            'score': self.score,
            'failures': self.failures,
            'details': self.details,
            'session_id': self.session_id,
            'game_id': self.game_id,
            'created_at': self.created_at.isoformat() if self.created_at else None,
            'updated_at': self.updated_at.isoformat() if self.updated_at else None,
        }