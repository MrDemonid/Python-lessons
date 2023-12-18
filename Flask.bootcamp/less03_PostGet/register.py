from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, EmailField, PasswordField
from wtforms.validators import DataRequired

# Создаём форму для регистрации пользователя
class RegisterForm(FlaskForm):
    name = StringField('Имя: ', validators=[DataRequired()])
    mail = EmailField('Эл. почта: ', validators=[DataRequired()])
    password = PasswordField('Пароль: ', validators=[DataRequired()])

    # validators - это какие проверки необходимо выполнять при вводе данных в поле
    # DataRequired() не даст ввести пустое поле.
    # но по хорошему регистрацию лучше проводить с помощью
    # модуля flask-login

    # создаём кнопку регистрации, чтобы распознать когда пользователь
    # отправит свои данные для регистрации
    submit = SubmitField('Зарегистрироваться')
    
