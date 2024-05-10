class Field:
    """
    Базовий клас для полів запису.
    """
    def __init__(self, value: str)-> None:
        """
        Конструктор класу, який приймає значення поля.
        """
        self.value = value

    def __str__(self):
        """
        Метод для перетворення об'єкта в рядок.
        """
        return str(self.value)