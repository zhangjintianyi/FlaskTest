from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,BooleanField,SubmitField
from wtforms.validators import Required, Length, Email, Regexp, EqualTo


class LoginForm(FlaskForm):
    email = StringField("邮箱", validators=[Required(),Length(1,64),Email()])
    username = StringField("用户名", validators=[Required()])
    password = PasswordField("密码",validators=[Required()])
    remember_me = BooleanField("记住登录")
    submit = SubmitField("登录")

class RegForm(FlaskForm):
    email = StringField("邮箱", validators=[Required(),Length(1,64),Email()])
    username = StringField("用户名", validators=[Required(),Length(1,64), Regexp("^[A-Za-z][A-za-z0-9_]+$",message="只能是大小写字母和下划线")])
    password = PasswordField("密码",validators=[Required()])
    password2 = PasswordField("确认密码", validators=[Required(), EqualTo("password", message="两次输入密码不一致")])
    submit = SubmitField("注册")