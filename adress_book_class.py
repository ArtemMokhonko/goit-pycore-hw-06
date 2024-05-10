from collections import UserDict
from record_class import Record

class AddressBook(UserDict):
    """
    Клас для зберігання та управління записами.
    """
    def add_record(self, record: Record):
        """
        Метод для додавання запису до адресної книги.
        """
        self.data[record.name.value] = record
        

    def find(self, name):
        """
        Метод для пошуку запису за іменем.
        """
        return self.data.get(name)


    def delete(self, name):
        """
        Метод для видалення запису за іменем.
        """
        if name in self.data:
            del self.data[name]