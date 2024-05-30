class ObjList:
    def __init__(self, data, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev

    def set_next(self, obj):
        self.next = obj

    def set_prev(self, obj):
        self.prev = obj

    def get_next(self):
        return self.next

    def get_prev(self):
        return self.prev

    def set_data(self, data):
        self.data = data

    def get_data(self):
        return self.data

    def __str__(self):
        return f'{self.data}'


class LinkedList:
    def __init__(self):
        self.lst = []
        self.head = None
        self.tail = None

    def add_obj(self, obj):
        new_obj = ObjList(obj)
        if self.head is None:
            self.head = new_obj
            self.tail = new_obj
        else:
            self.tail.next = new_obj
            new_obj.prev = self.tail
            self.tail = new_obj

    def get_data(self):
        current = self.head
        total = []
        while current:
            total.append(str(current.get_data()))
            current = current.next
        return total
