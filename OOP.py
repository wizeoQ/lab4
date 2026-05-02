import wizeo_lib as wiz


# Инкапсуляция
class BankAccount:
    def __init__(self, account_number, balance):
        # Публичный атрибут
        self.account_number = account_number
        # Приватный атрибут
        self.__balance = balance


    def deposit(self, amount):
        # Метод для увеличения баланса
        self.__balance += amount
        print(f"Внесено {amount}. Баланс: {self.__balance}")


    def get_balance(self):
        # Метод для получения текущего баланса
        return self.__balance


# Пример использования
account = BankAccount("88005553535", 20926)
account.deposit(67)
print(account.get_balance())
# account.__balance #Ошибка: приватный аттрибут не выведется.

wiz.l()
# Наследование
class Animal:
    def __init__(self, name):
        # Общий атрибут для всех животных
        self.name = name


    def speak(self):
        # Базовый метод: Общий для всех животных.
        return f"{self.name} произносит звук"
    
class Dog(Animal):
    def speak(self):
        # Переопредление метода для класса Dog
        return f"{self.name} лает."

class Cat(Animal):
    def speak(self):
        # Переопределение метода для класса Cat
        return f"{self.name} мурчит."
# Пример использования
dog = Dog("Кот")
cat = Cat("Собака")
print(dog.speak())
print(cat.speak())