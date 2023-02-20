from IPAddress import *
from NetWork import *


def task45(address: IPAddress):
    print(address.represent())
    print(f"This IP address is {address.determine_class()} Class")
    boundaries = address.boundary_addresses()
    print(f"Starting address: {boundaries[0]}")
    print(f"Ending address: {boundaries[1]}")
    print(f"Mask of {address}: {address.get_mask_by_class()}")


def task6(address: IPAddress, req_hsts, req_subnets):
    network = NetWork(address)
    print(
        f"Адрес сети: {address.represent()}\n"
        f"Кол-во необходимых подсетей: {req_subnets}\n"
        f"Кол-во необходимых хостов: {req_hsts}")
    print(f"Mask of subnet: {insert_dots(network.get_mask())}")
    print(f"Class of subnets: {network.find_subnet_class()}")
    print(f"Start of network: {network.find_start()}")
    print(f"End of network: {network.find_end()}")
    print(f"Count of IP: {network.count_addresses()}")
    print(f"Count of hosts: {network.count_hosts()}")
    network.first_five_addresses()
    network.last_five_addresses()


def main():
    task = int(input("Какое задание вы хотите решить?\n1) 4,5 задания\n2) 6 задание"))
    if task == 1:
        address = input("Введите IP-адрес: ")
        addr = IPAddress(address)
        task45(addr)
    elif task == 2:
        address = input("Введите IP-адрес сети: ")
        addr = IPAddress(address)
        hsts = input("Введите нужное количество хостов")
        subnets = input("Введите нужное количество подсетей")
        task6(addr, hsts, subnets)


if __name__ == '__main__':
    main()
