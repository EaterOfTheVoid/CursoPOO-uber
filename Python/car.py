from account import Account

class car:
    id = int
    license = str
    driver = Account("","")
    passegenger = int

    def __init__(self, license, driver):
        self.license    = license
        self.driver     = driver