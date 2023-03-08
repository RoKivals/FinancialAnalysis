class Bank:
    def __init__(self):
        self.accounts = []

    def add_account(self, money):
        self.accounts.append(money)
        print(f"Вы завели аккаунт №{len(self.accounts) - 1} и положили на него {money} у.е.")

    def money_change(self, value):
        if len(self.accounts) > 0:
            acc_id = int(input(f"Введите id одного из ваших счетов, сумму которого вы хотите изменить на {value} у.е.\n"
                               f"Номера всех ваших счетов:{' '.join(i for i in self.accounts)}"))
            self.accounts[acc_id] += value
        else:
            print("К сожалению, ни одного счёта не было найдено")

    def __str__(self):
        res = f"Информация о клиенте\nКол-во счетов: {len(self.accounts)}\n"
        for num, i in enumerate(self.accounts):
            if i is not None:
                res += f"Счёт №{num} хранит {i} у.е.\n"
        return res


def main():
    pass


if __name__ == '__main__':
    main()
