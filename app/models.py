from app import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from datetime import datetime
from . import login_manager



class User(UserMixin, db.Model):
    """用户表"""
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True)
    email = db.Column(db.String(64), nullable=False, index=True)
    username = db.Column(db.String(64), unique=True, index=True)
    password_hash = db.Column(db.String(128))
    posts = db.relationship('Post', backref='author', lazy='dynamic')

    #用户信息
    realname = db.Column(db.String(64))
    location = db.Column(db.String(64))
    about_me = db.Column(db.Text())
    register_since = db.Column(db.DateTime(), default=datetime.now())
    last_seen= db.Column(db.DateTime(), default=datetime.now())

    @property
    def password(self):
        raise 'password is not a readable attribute'

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password=password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return "<User_id:%d, User_name:%s, email:%s>" % (self.id, self.username, self.email)

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    def update_visit_time(self):
        self.last_seen = datetime.now()
        db.session.add(self)


class Post(db.Model):
    """博客表"""
    __tablename__ = "posts"
    id = db.Column(db.Integer, nullable=False, primary_key=True, autoincrement=True, index=True)
    title = db.Column(db.String(50), nullable=False)
    body = db.Column(db.Text)
    timestamp = db.Column(db.DateTime, default=datetime.now(), index=True)
    auth_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)


    def __init__(self, title, body, auth_id):
        self.title = title
        self.body = body
        self.auth_id = auth_id


    def __repr__(self):
        return "<Post_id:%d, Post_title:%s>" % (self.id, self.title)

