class Departament:
    id: int
    title: str

    # определяем конструктор
    def __init__(self, id: int, title: str) -> None:
        self.id = id
        self.title = title

    # определяем вывод объекта
    def __repr__(self) -> str:
        return f'id = {self.id} title = {self.title}'
    