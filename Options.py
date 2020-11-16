import sys
import File


def Mod():
    while True:
        try:
            mod = int(input('[1] Encrypt\n[2] Decryption\n[0] Exit\n\n-> '))

            if mod == 1 or mod == 2:
                return mod
            elif mod == 0:
                sys.exit()
            else:
                print("\n------ Invalid option ------\n")
        except ValueError:
            print("\n------ Invalid option ------\n")


def Key(totalKeys):
    finalKey = []
    count = 0

    print("\n------ Choose your keys ------")

    while count < totalKeys:
        try:
            key = int(input(f"\nEnter the {count + 1}/{totalKeys} key (1 to 9999999)\n-> "))

            if key in finalKey:
                print("\n------ Invalid key. Please enter a different key ------")
                continue

            if 0 < key < 10000000:
                finalKey.append(key)
                count += 1
            else:
                print("\n------ Invalid key. Please enter a valid key ------")

        except ValueError:
            print("\n------ Invalid key. Please enter a valid key ------")

    return finalKey


def QuantityKeys():
    while True:
        try:
            print("\n------ How many keys would you like? (3 to 20) ------\n")
            keys = int(input("-> "))

            if 2 < keys < 21:
                return keys
            else:
                print("\n------ Invalid option ------\n")
        except ValueError:
            print("\n------ Invalid option ------\n")


def FilePath():
    while True:
        try:
            print("------ Would you like to open a file? ------\n")
            option = int(input('[1] Yes\n[2] No\n\n-> '))

            if option == 1:
                fileName = File.SelectFile()

                if fileName == "":
                    continue

                return fileName
            elif option == 2:
                return ""
            else:
                print("\n------ Invalid option ------\n")
        except ValueError:
            print("\n------ Invalid option ------\n")


def SaveMessage1(path, message):
    while True:
        try:
            print("------ Would you like to save your message in a new file or in this file? ------\n")
            fileSituation = int(input("[1] New file\n[2] This file\n[0] Don't save \n-> "))

            if fileSituation == 1:
                fileName = File.CreateFile()

                if fileName == "":
                    continue

                File.WriteFile(fileName, message)
                break
            elif fileSituation == 2:
                File.WriteFile(path, message)
                break
            elif fileSituation == 0:
                break
            else:
                print("\n------ Invalid option ------\n")
        except ValueError:
            print("\n------ Invalid option ------\n")


def SaveMessage2(message):
    while True:
        try:
            print("------ Would you like to create a new file with your message? ------\n")
            fileSituation = int(input('[1] Yes\n[2] No\n\n-> '))

            if fileSituation == 1:
                fileName = File.CreateFile()

                if fileName == "":
                    continue

                File.WriteFile(fileName, message)
                break
            elif fileSituation == 2:
                break
            else:
                print("\n------ Invalid option ------\n")
        except ValueError:
            print("\n------ Invalid option ------\n")
