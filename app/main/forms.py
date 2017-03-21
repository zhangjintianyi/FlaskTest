from flask_wtf import FlaskForm
from wtforms.validators import Required, Length
from wtforms import TextField, TextAreaField, SubmitField, StringField, FileField

class PostForm(FlaskForm):
    title = TextField("标题", validators=[Required(), Length(1,50)])
    boby = TextAreaField("内容", validators=[Required()])
    submit = SubmitField("提交")

class EditInfoForm(FlaskForm):
    realname = StringField("真实姓名", validators=[Length(0,64)])
    location = StringField("所在城市", validators=[Length(0,64)])
    about_me = TextAreaField("自我介绍")
    submit = SubmitField("提交")
    favicon = FileField("上传头像")
    submit = SubmitField("上传头像")