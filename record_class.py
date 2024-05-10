from name_phone_class import Phone, Name

class Record:
    """
    Клас для зберігання інформації про контакт.
    """
    def __init__(self, name):
        """
        Конструктор класу, який приймає ім'я контакту.
        """
        self.name = Name(name)
        self.phones = []
        
        

    def add_phone(self, phone):
        """
        Метод для додавання телефону до запису.
        """
        if not self.find_phone(phone):
            self.phones.append(Phone(phone))
        

    def remove_phone(self, phone):
        """
        Метод для видалення телефону з запису.
        """
        self.phones = [p for p in self.phones if p.value != phone]

    def edit_phone(self, old_phone, new_phone):
        """
        Метод для редагування телефону в записі.
        """
        for i, phone in enumerate(self.phones):
            if phone.value == old_phone:
                self.phones[i] = Phone(new_phone) 
                        
        
    def find_phone(self, phone):
        """
        Метод для пошуку телефону в записі.
        """
        for p in self.phones:
            if p.value == phone:
                return p
        return None

    def __str__(self):
        """
        Метод для перетворення об'єкта в рядок для виводу.
        """
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"