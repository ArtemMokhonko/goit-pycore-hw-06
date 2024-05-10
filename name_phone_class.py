import re
from field_class import Field



class Name(Field):
    """
    Клас для зберігання імені контакту.
    """
    def __init__(self, name: str)-> None:
        """
        Конструктор класу, який приймає значення поля.
        Перевіряє, чи ім'я починається з великої літери і чи його довжина більша за 2 літери.
        """
        if not name[0].isupper():
            raise ValueError("Name must start with a capital letter")
        if len(name) <= 2:
            raise ValueError("Name must be longer than 2 letters")
        super().__init__(name)
        


class Phone(Field):
    """
    Клас для зберігання номера телефону.
    """
    def __init__(self, phone):
        """
        Конструктор класу, який приймає значення поля.
        Перевіряє валідність номера телефону.
        """
        if not re.fullmatch(r'\d{10}', phone):
            raise ValueError("Phone number must be 10 digits")
        super().__init__(phone)