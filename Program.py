import Options
import Message

print("------ Welcome to the Encryption ------\n")

while True:
    mod = Options.Mod()

    print("\n------ Choose your keys ------")
    key = Options.Key()

    print("\n------ Input your message ------\n")
    message = input("-> ")

    print(f"\nYour message:\n{Message.finalMessage(mod, key, message)}\n")
