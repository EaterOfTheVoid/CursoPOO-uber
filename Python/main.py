from car import car

if __name__ == "__main__":
    print("Hola Mundo")
    Car = car()
    Car.license = "SDT200"
    Car.driver = "Joaquin Blanco"
    print(vars(Car))

    car2 = car()
    car2.license = "Lpm444"
    car2.driver = "Ivan Reynoso"
    print(vars(car2))