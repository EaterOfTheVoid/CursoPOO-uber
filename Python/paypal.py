from payment import Payment

class paypal(Payment):
    id = int
    ref = str

    def __init__(self, id, ref):
        super().__init__(id)
        self.ref = ref;