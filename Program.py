import Options
import File
import Message

print("------ Welcome ------\n")

while True:
    mod = Options.Mod()
    totalKeys = Options.QuantityKeys()
    key = Options.Key(totalKeys)
    path = Options.FilePath()

    if path == "":
        print("\n------ Input your message ------\n")
        message = input("-> ")
    else:
        message = File.Read(path)

    message = Message.finalMessage(mod, key, message, totalKeys)

    print(f"\nYour message:\n{message}\n")

    if path != "":
        Options.SaveMessage1(path, message)
    else:
        Options.SaveMessage2(message)

    print("\n------ Thank you! ------\n")
