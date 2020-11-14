import LetterAccent
import Calculate
import Cryptography

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26]


def finalMessage(mod, key, msg):
    message = ''
    i = 0

    for letter in msg:

        if letter.upper() not in ('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
                                  'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'):
            letter = LetterAccent.remove(letter)

        if letter.isalpha():
            n1 = ord(letter.upper())
            n2 = numbers[Calculate.getLetterNumber(letter)]
            n3 = key[i]

            difference = Calculate.getDifference(abs(n1 - n2 - n3))

            i += 1
            if i == 3:
                i = 0

            message += Cryptography.msgCryptography(n2, difference, mod).upper() if letter.isupper() else \
                Cryptography.msgCryptography(n2, difference, mod).lower()
        else:
            message += letter

    return message








