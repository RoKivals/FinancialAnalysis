from IPAddress import *


class NetWork:
    def __init__(self, address: IPAddress):
        self.net_address = address
        self.brought_bits = 0
        self.subnet_mask = None
        self.net_address.get_mask_by_class()

    # cnt of IP addresses in subnet
    def count_addresses(self):
        return 2 ** (32 - self.net_address.prefix - self.brought_bits)

    # cnt of hosts available IP addresses in subnet
    def count_hosts(self):
        return 2 ** (32 - self.net_address.prefix - self.brought_bits) - 2

    def count_subnets(self):
        return 2 ** self.brought_bits

    def find_required_subnet(self, req_subnets, req_hosts):
        if req_hosts > self.count_hosts():
            raise Exception('It\'s impossible to make so many hosts')
        while self.count_subnets() < req_subnets and self.count_hosts() * self.count_subnets() > req_hosts:
            self.brought_bits += 1
        while self.count_hosts() * self.count_subnets() > req_hosts:
            self.brought_bits += 1

    def find_subnet_class(self) -> str:
        # C - class of subnets
        if 32 >= self.net_address.prefix + self.brought_bits > 24:
            return f'C * 2 ^ (1/{(self.net_address.prefix + self.brought_bits - 24)})'
        if 24 >= self.net_address.prefix + self.brought_bits > 16:
            return f'C * {2 ** (24 - self.net_address.prefix + self.brought_bits)}'

        # B - class of subnet
        if 16 >= self.net_address.prefix + self.brought_bits > 8:
            return f'B * {2 ** (16 - self.net_address.prefix + self.brought_bits)}'

        # A - class of subnet
        if 8 >= self.net_address.prefix + self.brought_bits >= 0:
            return f'A * {2 ** (8 - self.net_address.prefix + self.brought_bits)}'

    def find_start(self):
        s = self.net_address.get_binary_represent()
        s = '.'.join(i for i in s[::8])
        return s

    def find_end(self):
        s = self.net_address.get_binary_represent()
        s = s[:self.net_address.prefix]
        s = s + "".join('1' * (32 - self.net_address.prefix))
        s = '.'.join(f'{int(i, 2)}' for i in s[::8])
        return s
