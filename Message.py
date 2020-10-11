import Calc


def finalMessage(mod, key, alphabet, msg):
    message = ''
    i = 0

    for letter in msg:
        if letter.isalpha():
            n1 = ord(letter.upper())
            n2 = alphabet[Calc.getLetterNumber(letter)]
            n3 = key[i]

            difference = Calc.getDifference(abs(n1 - n2 - n3))

            i += 1
            if i == 3:
                i = 0

        else:
            message += letter
