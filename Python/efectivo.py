from payment import Payment

class efectivo(Payment):
    id = int

    def __init__(self, id):
        super().__init__(id)