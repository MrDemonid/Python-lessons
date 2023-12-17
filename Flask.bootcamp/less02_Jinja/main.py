from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    # отдадим html-файл нашей главной страницы, поменяв 
    # переменную {{mytitle}} на строку 'Главная страница'
    return render_template('index.html', mytitle='Главная страница')

@app.route("/students")
def info():
    list_std = ['Андрей Хлус',
                'Олег Антончик', 
                'Наталья Василенко',
                'Maria Andreeva',
                'Алексей Виноградов',
                'Антон Панфилов',
                'Евгений Коростелев',
                'Михаил Кудрявцев']
    return render_template('students.html', stydents=list_std, title='Студенты на занятии')


if __name__ == '__main__':
    app.run()

