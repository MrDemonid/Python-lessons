from flask import Flask, render_template, redirect
from login import LoginForm
from register import RegisterForm
from data import db_session, users
# from flask_login import login_user
# from werkzeug.security import generate_password_hash


app = Flask(__name__)
app.config["SECRET_KEY"]= "MY SECRET KEYS FOR HOME COMPUTER"


@app.route("/")
def index():
    # отдадим html-файл нашей главной страницы, поменяв 
    # переменную {{mytitle}} на строку 'Главная страница'
    return render_template('index.html', mytitle='Главная страница')

@app.route("/students")
def showStydents():
    list_std = ['Андрей Хлус',
                'Олег Антончик', 
                'Наталья Василенко',
                'Maria Andreeva',
                'Алексей Виноградов',
                'Антон Панфилов',
                'Евгений Коростелев',
                'Михаил Кудрявцев']
    return render_template('students.html', stydents=list_std, title='Студенты на занятии')


'''
    Страница (форма) регистрации
'''
@app.route("/register", methods = ["GET", "POST"])
def regNewUser():
    db_session.global_init('db/blogs.sqlite')   # открываем БД
    frm=RegisterForm()
    if frm.validate_on_submit():
        # нажали кнопку "Зарегистрироваться"
        # print("register: ", frm.data["name"], frm.data["mail"], frm.data["password"])
        try: # обработка исключений
            sessions = db_session.create_session()
            # создаём объект класса User
            user = users.User(
                name=frm.name.data,
                email=frm.email.data,
                telephone=frm.telephone.data,
                password=frm.password.data
            )
            # создаём хэш пароля
            user.set_password(frm.password.data)
            # и отправляем данные в БД
            sessions.add(user)
            sessions.commit()
        except:
            return render_template('register.html', message='Такой пользователь уже есть!')
        return render_template('index.html', mytitle='Главная страница', message='Вы зарегистрировались!')
    return render_template('register.html', form=frm)


'''
    Страница (форма) авторизации
'''
@app.route("/auth", methods = ["GET", "POST"])
def loginUser():
    db_session.global_init('db/blogs.sqlite')
    frm = LoginForm()
    if frm.validate_on_submit():
        # print("auth: ", frm.data["name"], frm.data["password"])
        sessions = db_session.create_session()
        user = sessions.query(users.User).filter(users.User.email == frm.email.data).first()
        if user and user.password == frm.password.data:
            # login_user(user, remember=form.remember_me.data)
            return redirect('/')
        return render_template("auth.html", message="Пользователь не найден")
    return render_template('auth.html', form=frm)


if __name__ == '__main__':
    db_session.global_init('db/blogs.sqlite')
    app.run()

