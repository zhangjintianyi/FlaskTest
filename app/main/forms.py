from flask_wtf import FlaskForm
from wtforms.validators import Required, Length
from wtforms import TextField, TextAreaField, SubmitField

class PostFrom(FlaskForm):
    title = TextField("标题", validators=[Required(), Length(1,50)])
    boby = TextAreaField("内容", validators=[Required()])
    submit = SubmitField("提交")