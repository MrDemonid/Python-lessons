from Worker import Worker
from Departament import Departament

class DataBase:
    worker_table: list[Worker]      # список всех рабочих
    dep_table: list[Departament]    # список всех департаментов

    # определяем конструктор
    def __init__(self) -> None:
        self.worker_table = []      # создаем пустые списки
        self.dep_table = []

    # добавление рабочего
    def append_worker(self, worker: Worker) -> None:
        self.worker_table.append(worker)

    # добавление департамента
    def append_dep(self, dep: Departament) -> None:
        self.dep_table.append(dep)

    # определяем выборку по всем рабочим
    def select_all_worker(self) -> str:
        output: str = ""
        for w in self.worker_table:
            output += f'{w.full_name} {w.age}\n'
        return output
    
    # определяем выборку по всем департаментам
    def select_all_dep(self) -> str:
        output: str = ""
        for dep in self.dep_table:
            output += f'{dep.title}\n'
        return output
    
    # определяем создание кортежа из имени рабочих, их возраста и места их работы
    def report(self) -> list[tuple]:
        rep: list[tuple] = []
        for w in self.worker_table:
            rep.append((w.full_name, w.age, self.dep_table[w.dep_id].title))
        return rep
    