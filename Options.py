import sys


NORMAL_TEXT = "\033[0m"
COLOR_RED = "\033[31m"


def Mod():
    while True:
        try:
            mod = int(input('[1] Encrypt\n[2] Decryption\n[0] Exit\n\n-> '))

            if mod == 1 or mod == 2:
                return mod
            elif mod == 0:
                sys.exit()
            else:
                print(COLOR_RED + "\n------ Invalid option ------\n" + NORMAL_TEXT)
        except ValueError:
            print(COLOR_RED + "\n------ Invalid option ------\n" + NORMAL_TEXT)


def Key(totalKeys):
    finalKey = []
    count = 0

    print("\n------ Choose your keys ------")

    while count < totalKeys:
        try:
            key = int(input(f"\nEnter the {count + 1}/{totalKeys} key (1 to 9999999)\n-> "))

            if key in finalKey:
                print(COLOR_RED + "\n------ Invalid key. Please enter a different key ------" + NORMAL_TEXT)
                continue

            if 0 < key < 10000000:
                finalKey.append(key)
                count += 1
            else:
                print(COLOR_RED + "\n------ Invalid key. Please enter a valid key ------" + NORMAL_TEXT)

        except ValueError:
            print(COLOR_RED + "\n------ Invalid key. Please enter a valid key ------" + NORMAL_TEXT)

    return finalKey


def HowManykeys():
    while True:
        try:
            print("\n------ How many keys would you like? (3 to 20) ------\n")
            keys = int(input("-> "))

            if 2 < keys < 21:
                return keys
            else:
                print(COLOR_RED + "\n------ Invalid option ------\n" + NORMAL_TEXT)
        except ValueError:
            print(COLOR_RED + "\n------ Invalid option ------\n" + NORMAL_TEXT)

