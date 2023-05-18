from payment import Payment

class tarjeta(Payment):
    id = int
    cvv = int
    FDV = str

    def __init__(self, id, cvv, FDV):
        super().__init__(id)
        self.FDV = FDV
        self.cvv = cvv