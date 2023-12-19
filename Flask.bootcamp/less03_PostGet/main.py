from flask import Flask, render_template
from register import RegisterForm
from login import LoginForm

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

@app.route("/reg", methods = ["GET", "POST"])
def regNewUser():
    frm=RegisterForm()
    if frm.validate_on_submit():
        print("register: ", frm.data["name"], frm.data["mail"], frm.data["password"])
    return render_template('register.html', form=frm)

@app.route("/auth", methods = ["GET", "POST"])
def loginUser():
    frm = LoginForm()
    if frm.validate_on_submit():
        print("auth: ", frm.data["name"], frm.data["password"])
    return render_template('auth.html', form=frm)



if __name__ == '__main__':
    app.run()

