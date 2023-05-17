class Main {
    public static void main(String[] args) {
        System.out.println("Hola Mundo");

        Car car = new Car();
        car.license = "BRO321";
        car.driver = "Martin Fierro";
        car.passenger = 2;
        car.printDataC();

        Car car2 = new Car();
        car2.license = "sHu371";
        car2.driver = "Marta Pedran";
        car2.passenger = 1;
        car.printDataC();
    }
}