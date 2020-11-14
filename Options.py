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


def Key():
    finalKey = []
    count = 0

    while count < 3:
        try:
            key = int(input(f"\nEnter the {count + 1}/3 key (1 to 9999999)\n-> "))

            if 0 < key < 10000000:
                finalKey.append(key)
                count += 1
            else:
                print(COLOR_RED + "\n------ Invalid key. Please enter a valid key ------" + NORMAL_TEXT)
        except ValueError:
            print(COLOR_RED + "\n------ Invalid key. Please enter a valid key ------" + NORMAL_TEXT)

    return finalKey
