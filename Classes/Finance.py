class Finance:
    def __init__(self, salary, tax):
        self.salary = salary
        self.tax = tax

    def get_income_amount(self):
        return self.salary * (self.tax / 100)

    def get_net_salary(self):
        return self.salary - self.get_income_amount()
