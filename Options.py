def Mod():
    while True:
        mod = int(input('[1] Encrypt\n[2] Decryption\n\n-> '))

        if mod == 1 or mod == 2:
            return mod
        else:
            print("Invalid option\n")


def Key():
    key = []
    tmp = 0

    while tmp < 3:
        x = int(input(f"Enter the {tmp + 1}/3 key (1 to 9999)\n-> "))

        if 0 < x < 10000:
            key.append(x)
            tmp += 1
        else:
            print("Invalid option\n")

    return key
