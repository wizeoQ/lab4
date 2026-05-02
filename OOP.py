import wizeo_lib as wiz
from typing import Union

# Инкапсуляция
wiz.l()
class Vehicle:
    def __init__(self, 
                 speed: Union[int,float], 
                 fuel: float) -> None:
        self.speed = speed
        if speed < 0: raise ValueError ("Значение скорости некорректно.")
        self.__fuel = fuel
        if not (0 <= fuel <=100):
            raise ValueError ("Значение топлива некорректно.")
            
    def get_speed(self):
        if self.__fuel == 0:
            self.speed = 0
        print(f"Скорость - {self.speed}")

    def get_fuel(self):
        print(f"Бак заполнен на {self.__fuel}%")
    
    def waste_fuel(self, amount):
        self.__fuel -= amount
        if self.__fuel < 0:
            self.__fuel = 0
        print(f"Бензин потрачен на {amount}%\
              "f"\nБак заполнен на {self.__fuel}%")
    
    def add_fuel(self, amount):
        self.__fuel += amount
        if self.__fuel > 100:
            self.__fuel = 100
        print(f"В бак добавлено {amount}% бензина\
              "f"\nБак заполнен на {self.__fuel}%")
    def set_fuel(self):
        self.__fuel = 100
        print("Бак заполнен")


car = Vehicle(120, 100)
car.get_fuel()
car.get_speed()
car.waste_fuel(10)
car.waste_fuel(20)
car.waste_fuel(30)
car.waste_fuel(40)
car.get_speed()
car.add_fuel(130)
car.speed = 230
car.get_speed()
car.__fuel = 70
car.get_fuel()

wiz.l()
