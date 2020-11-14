import Options
import Message

print("------ Welcome to the Encryption ------\n")

while True:
    mod = Options.Mod()
    totalKeys = Options.HowManykeys()
    key = Options.Key(totalKeys)

    print("\n------ Input your message ------\n")
    message = input("-> ")

    print(f"\nYour message:\n{Message.finalMessage(mod, key, message, totalKeys)}\n")
