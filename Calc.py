def getLetterNumber(letter):
    number = ord(letter.lower()) - 97
    return number


def getDifference(x):
    i = 1
    result = 0

    while 26 * i < x:
        result = 26 * i
        i += 1

    return abs(result - x)
