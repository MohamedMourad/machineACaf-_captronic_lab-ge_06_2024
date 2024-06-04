class coffe_machine:
    def __init__(self, amount_of_money_inserted) -> None:
        self.amount_of_money_inserted = 0
        self.amount_of_coffe_to_prepare = 0
        self.name = "coffe_machine_simple"
        pass

    def insert(self, money):
        self.amount_of_money_inserted = money
        pass

    def amount_of_coffe_to_prepare(self):
        return self.amount_of_coffe_to_prepare


