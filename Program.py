import Options
import Message

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26]

print("------ Welcome to the Encryption ------\n")
mod = Options.Mod()

print("------ Choose your keys ------\n")
key = Options.Key()
alphabet = numbers

print("------ Input your message ------\n")
msg = input("Enter the message\n-> ")

print(f"\nYour message: {Message.finalMessage(mod, key, alphabet, msg)}")

