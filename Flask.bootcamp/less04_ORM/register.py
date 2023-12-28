from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, EmailField
from wtforms.validators import DataRequired

# Создаём форму для регистрации пользователя
class RegisterForm(FlaskForm):
    email = EmailField('Почта', validators=[DataRequired()])
    password = PasswordField('Пароль', validators=[DataRequired()])
    password_again = PasswordField('Повторите пароль', validators=[DataRequired()])
    name = StringField('Имя пользователя', validators=[DataRequired()])
    telephone = StringField('Телефон', validators=[DataRequired()])

    # validators - это какие проверки необходимо выполнять при вводе данных в поле
    # DataRequired() не даст ввести пустое поле.
    # но по хорошему регистрацию лучше проводить с помощью
    # модуля flask-login

    # создаём кнопку регистрации, чтобы распознать когда пользователь
    # отправит свои данные для регистрации
    submit = SubmitField('Зарегистрироваться')
    