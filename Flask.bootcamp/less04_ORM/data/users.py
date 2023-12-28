import datetime
import sqlalchemy
from sqlalchemy import orm
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from .db_session import SqlAlchemyBase
from sqlalchemy_serializer import SerializerMixin

'''
    Привязка ORM-модели к конкретной таблицу. Для каждой таблицы выполняется 
своя привязка.
'''
class User(SqlAlchemyBase, UserMixin, SerializerMixin):
    __tablename__ = 'users'         # имя таблицы в БД

    '''
        Привязываем переменные к столбцам таблицы. Имена переменных и столбцов
    должны совпадать.
    primary_key - уникальный идентификатор (True - да)
    autoimcrement - увеличивать ли автоматически значение счетчика при добавлении новых данных
    nullable - флаг допустимости пустого поля (True - не допустимо)
    unique - флаг наличия дублей значений в полях (True - совпадения запрещены)
    default - значение по умолчанию (datetime.now() - вызвращает текущую дату и время)
    '''
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    name = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    email = sqlalchemy.Column(sqlalchemy.String, index=True, unique=True, nullable=True)
    password = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    telephone = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    created_date = sqlalchemy.Column(sqlalchemy.DateTime, default=datetime.datetime.now)

    # методы класса

    # создаёт хеш пароля
    def set_password(self, password):
        self.hashed_password = generate_password_hash(password)

    # проверяет пароль и его хеш на корректность
    def check_password(self, password):
        return check_password_hash(self.hashed_password, password)

    # вывод объекта класса на консоль посредством print()
    def __repr__(self):
        return f'{self.id}, {self.name}, {self.telephone}, {self.email}'
