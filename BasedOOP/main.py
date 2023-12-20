from Worker import Worker
from Departament import Departament
from DataBase import DataBase

db: DataBase = DataBase()

db.append_dep(Departament(0, 'Информационные технологии'))
db.append_dep(Departament(1, 'Отдел кадров'))
db.append_dep(Departament(2, 'Бухгалтерия'))

db.append_worker(Worker(0, 'Мария Ивановна', 23, 1234, 2))
db.append_worker(Worker(1, 'Мария Степанова', 26, 3456, 0))
db.append_worker(Worker(2, 'Василий Петров', 33, 3458, 2))
db.append_worker(Worker(3, 'Игнат Васильев', 33, 5822, 0))
db.append_worker(Worker(4, 'Ольга Петрова', 31, 3234, 1))

print(db.select_all_dep())
print(db.select_all_worker())

# выведем сводные данные по всем работникам
for i in db.report():
    print(i)

print('done!')
