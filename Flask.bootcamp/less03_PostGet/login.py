from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired

# Создаём форму для авторизации пользователя
class LoginForm(FlaskForm):
    name = StringField('Имя: ', validators=[DataRequired()])
    password = PasswordField('Пароль: ', validators=[DataRequired()])
    submit = SubmitField('Войти')
