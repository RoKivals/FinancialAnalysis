from IPAddress import *


def task5(address: IPAddress):
    print(address.represent())
    print(f"This IP address is {address.determine_class()} Class")
    boundaries = address.boundary_addresses()
    print(f"Starting address: {boundaries[0]}")
    print(f"Ending address: {boundaries[1]}")
    print(f"Mask of {address}: {address.get_mask_by_class()}")


def main():
    address = input("Введите IP-адрес: ")
    a = IPAddress(address)
    task5(a)


if __name__ == '__main__':
    main()
