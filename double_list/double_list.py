class ObjList:
    """Класс 'внутреннего' списка(более маленького)"""

    def __init__(self, data: str, next_elem=None, prev=None):
        """При первой инициализации ни следующих ни придыдущих объектов нет"""
        self.__data = data
        self.__next = next_elem
        self.__prev = prev

    def set_next(self, obj) -> None:
        """Устанавливает ссылку на следующее значение"""
        self.__next = obj

    def set_prev(self, obj) -> None:
        """Устанавливает ссылку на предыдущее значение"""
        self.__prev = obj

    def get_next(self):
        """Возвращает следущий объект"""
        return self.__next

    def get_prev(self):
        """Возвращает предыдущий объект"""
        return self.__prev

    def set_data(self, data) -> None:
        """Устанавливает значение для узла"""
        self.__data = data

    def get_data(self) -> str:
        """Возвращает значение узда"""
        return self.__data

    def __str__(self) -> str:
        """Возвращает представление в виде строки"""
        return f'{self.__data}'


class LinkedList:
    """Главный класс двусвязного списка"""

    def __init__(self):
        """Определяем значение головы, хвоста и масива для хранения элементов.
        При первой инициализации ни головы, ни хвоста нет."""
        self.lst = []
        self.head = None
        self.tail = None

    def add_obj(self, obj: ObjList) -> None:
        """Добавление нового элемента в двусвязный список и
        изменени ссылок на голову, хвост, предыдущий и следующий элемент"""
        new_obj = obj
        if self.head is None:
            self.head = new_obj
            self.tail = new_obj
        else:
            self.tail.set_next(new_obj)
            new_obj.set_prev(self.tail)
            self.tail = new_obj

    def get_data(self) -> list:
        current = self.head
        total = []
        while current:
            total.append(str(current.get_data()))
            current = current.get_next()
        return total


lst = LinkedList()
lst.add_obj(ObjList('данные 1'))
lst.add_obj(ObjList('данные 2'))
lst.add_obj(ObjList('данные 3'))
res = lst.get_data()
print(res)
