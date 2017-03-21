from flask import render_template, url_for, flash, redirect, abort,request
from . import main
from app.models import Post,User
from .forms import PostForm, EditInfoForm
from flask_login import login_required,current_user
from .. import db, ALLOWED_EXTENSIONS
import os

@main.route('/')
def index():
    posts = Post.query.order_by(Post.timestamp.desc()).all()
    return render_template("index.html", posts = posts)

@main.route('/user/<int:user_id>', methods=['GET', 'POST'])
@login_required
def person_center(user_id):
    form = PostForm()
    if form.validate_on_submit():
        post = Post(title=form.title.data, body=form.boby.data, auth_id=user_id) #current_user._get_current_object()
        db.session.add(post)                                                                                   #是获取model的对象，想要具体字段得用点
        posts = Post.query.filter_by(auth_id=current_user._get_current_object().id).order_by(Post.timestamp.desc()).all()
        form1 = PostForm
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

def allowed_file(file_name):
    return '.' in file_name and \
           file_name.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

@main.route('/user/<username>/edit_info', methods=['GET', 'POST'])
@login_required
def edit_userinfo(username):
    form = EditInfoForm()
    if form.validate_on_submit():
        current_user.realname = form.realname.data
        current_user.location = form.location.data
        current_user.about_me = form.about_me.data
        favicon_name = form.favicon.data
        print(os.path.join(r'C:\Users\Administrator\FlaskTest\FlaskTest\images', favicon_name.filename))
        if favicon_name and allowed_file(favicon_name):
            favicon_name.save(os.path.join(r'C:\Users\Administrator\FlaskTest\FlaskTest\images', favicon_name.filename), buffer_size=1024*30)
        db.session.add(current_user)
        flash('您的用户信息已更新')
        return redirect(url_for('main.show_userinfo', username=current_user.username))

    form.realname.data = current_user.realname
    form.location.data = current_user.location
    form.about_me.data = current_user.about_me
    return render_template('edit_info.html', form=form)


