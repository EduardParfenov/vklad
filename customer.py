
class Customer:

    def __init__(self, name, balance = 0):
        self.name = name
        self._balance = balance

    def __str__(self):
        return "Клиент \'{}\'. Баланс: {} рублей.".format(self.name, self.balance)

    @property
    def balance(self):
        return self._balance

    def record_payment(self, amount_paid):
        assert amount_paid > 0, "Сумма пополнения должна быть > 0!"
        self._balance += amount_paid

    def record_call(self, call_type, minutes):
        if call_type == 'Г':
            self._balance -= minutes * 5
        elif call_type == 'М':
            self._balance -= minutes * 1