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

    # find required mask for subnet
    def find_required_subnet(self, req_subnets, req_hosts):
        if req_hosts > self.count_hosts():
            raise Exception('It\'s impossible to make so many hosts')
        while self.count_subnets() < req_subnets and self.count_hosts() > req_hosts:
            self.brought_bits += 1
        while self.count_hosts() > req_hosts:
            self.brought_bits += 1
        else:
            self.brought_bits -= 1

    def get_mask(self):
        return '1' * (self.net_address.get_prefix() + self.brought_bits) + '0' * (
                    32 - self.net_address.get_prefix() + self.brought_bits)

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
        return s

    def find_end(self):
        s = self.net_address.get_binary_represent()
        s = s[:self.net_address.prefix]
        s = s + "".join('1' * (32 - self.net_address.prefix))
        return s

    def first_five_addresses(self):
        d = 5
        subnet = 0
        address = 1
        s = self.find_start()
        s_fixed = s[:self.net_address.prefix]
        s_mutable = s[self.net_address.prefix:]
        while d > 0:
            if address > self.count_addresses():
                address = 0
                subnet += 1
            s_mutable = f'{subnet:0{self.brought_bits}b}{address:0{32 - self.net_address.prefix - self.brought_bits}b}'
            address += 1
            if s_fixed + s_mutable != s:
                d -= 1
                print(s_fixed + s_mutable)

    def last_five_addresses(self):
        d = 5
        subnet = self.count_subnets()
        address = self.count_addresses()
        s = self.find_end()
        s_fixed = s[:self.net_address.prefix]
        s_mutable = s[self.net_address.prefix:]
        while d > 0:
            if address < 0:
                address = self.count_addresses()
                subnet -= 1
            s_mutable = f'{subnet:0{self.brought_bits}b}{address:0{32 - self.net_address.prefix - self.brought_bits}b}'
            address -= 1
            if s_fixed + s_mutable != s:
                d -= 1
                print(s_fixed + s_mutable)


def insert_dots(s: str):
    return f'{s[:8]}.{s[8:16]}.{s[16:24]}.{s[24:32]}'
