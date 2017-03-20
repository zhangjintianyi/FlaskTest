from flask import render_template, redirect, request, url_for, flash
from flask_login import login_user, logout_user, login_required

from app.models import User
from . import auth
from .forms import LoginForm, RegForm
from .. import db


@auth.route("/login", methods=["GET","POST"])
def Login():
    form = LoginForm()
    if form.validate_on_submit():
        user_info = User.query.filter_by(email=form.email.data).first()
        print(user_info)
        print(form.password.data)
        print(user_info.password_hash)
        #print(user_info.verify_paaword(form.password.data))
        if user_info is not None and user_info.verify_password(form.password.data):
            login_user(user_info, form.remember_me.data)
            flash('登录成功')
            return redirect(request.args.get("next") or url_for("main.index"))
        flash('无效的用户名或者密码')
    return render_template("login.html", form = form)

@auth.route("/logout")
@login_required
def Logout():
    logout_user()
    flash("已经退出登录")
    return redirect(url_for("main.index"))

@auth.route("/register", methods=["GET","POST"])
def Register():
    form = RegForm()
    if form.validate_on_submit():
        user = User(email=form.email.data, username=form.username.data, password=form.password.data)
        db.session.add(user)
        flash("请登录")
        return redirect(url_for("auth.Login"))
    return render_template("register.html",form = form)