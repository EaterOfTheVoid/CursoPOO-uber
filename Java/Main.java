class Main {
    public static void main(String[] args) {{

        System.out.println("Hola Mundo");
        Car car = new Car("BRO321", new Account("Martin Fierro", "AND123"));
        car.passegenger = 2;
        car.printDataC();

        Car car2 = new Car("sHu371", new Account("Marta Pedran", "ANDA876"));
        car2.passegenger = 3;
        car2.printDataC();
    }
}