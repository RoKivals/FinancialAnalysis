class IPAddress:
    def __init__(self, address: str):
        self.decimal_octets = []
        self.prefix = None
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

            try:
                self.prefix = int(address[address.index("\\") + 1:])
                if 0 > self.prefix > 32:
                    raise Exception("Use only numbers from 0 to 32 in prefix")
            except ValueError:
                raise Exception("You have used invalid symbols in prefix")
            self.mask = (1 << 32) - (1 << 32 >> self.prefix)
            address = address[:address.index("\\")]

        flag = ""
        # ----length---- #
        for cnt, octet in enumerate(address.split('.')):
            if len(octet) == 8:
                if flag == "Bin":
                    raise Exception(f"Use the same number system. Error in {cnt + 1} octet")
                flag = "Dec"
                try:
                    digit_octet = int(octet, 2)
                    self.decimal_octets.append(digit_octet)
                except ValueError:
                    raise Exception(f"Invalid symbol in {cnt + 1} octet")

            elif 1 <= len(octet) <= 3:
                if flag == "Dec":
                    raise Exception(f"Use the same number system. Error in {cnt + 1} octet")
                flag = "Bin"
                try:
                    digit_octet = int(octet)
                    if 255 < digit_octet < 0:
                        raise Exception(f"Еhe value can only be from 0 to 255. The error in {cnt + 1} octet")
                    self.decimal_octets.append(digit_octet)
                except ValueError:
                    raise Exception(f"Invalid symbol in {cnt + 1} octet")

            else:
                raise Exception(f"Invalid count of symbols in {cnt + 1} octet")

    def __str__(self):
        return ".".join(str(i) for i in self.decimal_octets)

    def represent(self):
        dec = "Decimal representation: " + ".".join(str(i) for i in self.decimal_octets)
        binary = "Binary representation: " + ".".join(f"{i:>08b}" for i in self.decimal_octets)
        return dec + '\n' + binary

    def find_class(self) -> str:
        if f"{self.decimal_octets[0]:08b}"[0] == '0':
            return 'A'

        if f"{self.decimal_octets[0]:08b}"[:2] == '10':
            return 'B'

        if f"{self.decimal_octets[0]:08b}"[:3] == '110':
            return 'C'

        if f"{self.decimal_octets[0]:08b}"[:4] == '1110':
            return 'D'

        if f"{self.decimal_octets[0]:08b}"[:4] == '1111':
            return 'E'

    def boundary_addresses(self) -> tuple:
        network_classes = {
            'A': ['0.0.0.0', '127.255.255.255'],
            'B': ['128.0.0.0', '191.255.255.255'],
            'C': ['192.0.0.0', '223.255.255.255'],
            'D': ['224.0.0.0', '239.255.255.255'],
            'E': ['240.0.0.0', '255.255.255.255']
        }
        return network_classes[self.find_class()][0], network_classes[self.find_class()][1]

    def find_mask(self):
        mask_classes = {
            'A': '255.0.0.0',
            'B': '255.255.0.0',
            'C': '255.255.255.0',
            'D': 'No mask, this IP address is using for group mailing',
            'E': 'No mask, this IP address is Reserved'
        }
        return mask_classes[self.find_class()]
