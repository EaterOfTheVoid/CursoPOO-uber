from car import car
from account import Account

if __name__ == "__main__":
    print("Hola Mundo")
    car1 = car("SDT200", Account("Joaquin Blanco", "42025921"))
    print(vars(car1))

    car2 = car("Lpm444", Account("Ivan Reynoso", "21411312"))
    print(vars(car2))