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