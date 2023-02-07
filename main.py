class IPAdress:
    def __init__(self, address: str):
        self.binary_octate = []
        self.decimal_octate = list(".".join(['0' for _ in range(4)]))
        self.mask = None

        # ----dots---- #
        if address.count('.') != 3:
            raise Exception("Invalid IP address")

        # ----slashes---- #
        if address.count("\\") > 1:
            raise Exception("Invalid count of \\")
        if address.count("\\") == 1:
            # finding \ in address (1.1.1.1\24)
            slash_pos_from_end = len(address) - address.index("\\")
            if slash_pos_from_end not in (2, 3):
                raise Exception("Invalid position for \\")
            self.mask = address[address.index("\\") + 1:]
            address = address[:address.index("\\")]

        # ----length---- #


def main():
    address = input("Введите IP-адрес")
    a = IPAdress(address)


if __name__ == '__main__':
    main()
