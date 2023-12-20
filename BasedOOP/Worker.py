class Worker:
    id: int             # id рабочего
    dep_id: int         # id департамента, где он работает
    age: int            # лет рабочему
    salary: int         # его зарплата
    full_name: str      # его полное имя

    # определяем конструктор
    def __init__(self, id: int, worker_name: str, age: int, salary: int, dep_id: int) -> None:
        self.id = id
        self.full_name = worker_name
        self.age = age
        self.salary = salary
        self.dep_id = dep_id

    # определяем красивый вывод, чтобы выводился объект с полями и тд.
    def __repr__(self) -> str:
        return f'id = {self.id} name = {self.full_name} age = {self.age} salary = {self.salary} departament = {self.dep_id}'
    