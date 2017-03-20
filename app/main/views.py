from flask import render_template, url_for, flash, redirect, abort
from . import main
from app.models import Post,User
from .forms import PostFrom
from flask_login import login_required,current_user
from .. import db

@main.route('/')
def index():
    posts = Post.query.order_by(Post.timestamp.desc()).all()
    return render_template("index.html", posts = posts)

@main.route('/user/<int:user_id>', methods=['GET', 'POST'])
@login_required
def person_center(user_id):
    form = PostFrom()
    if form.validate_on_submit():
        post = Post(title=form.title.data, body=form.boby.data, auth_id=user_id) #current_user._get_current_object()
        db.session.add(post)                                                                                   #是获取model的对象，想要具体字段得用点
        posts = Post.query.filter_by(auth_id=current_user._get_current_object().id).order_by(Post.timestamp.desc()).all()
        form1 = PostFrom
        return redirect(url_for("main.person_center", user_id=user_id, form=form1, posts=posts))
    posts = Post.query.filter_by(auth_id=user_id).order_by(Post.timestamp.desc()).all()
    return render_template('post.html', form=form, posts=posts)

@main.route('/user/<username>/info')
@login_required
def show_userinfo(username):
    user = User.query.filter_by(username=username).first()
    if user is None:
        abort(404)
    return render_template('user.html', user=user)

@main.route('/user/<username>/edit_info')
@login_required
def show_userinfo(username):
    user = User.query.filter_by(username=username).first()
    if user is None:
        abort(404)
    return render_template('edit_info.html', user=user)



