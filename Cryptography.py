def msgCryptography(letter, difference, mod):
    tmp = 0
    tmp2 = letter

    if mod == 1:
        while tmp2 < 26:
            tmp += 1
            tmp2 += 1
    else:
        while tmp2 > 1:
            tmp += 1
            tmp2 -= 1

    if difference > tmp:
        difference = abs(difference - tmp)

        return letters[difference - 1] if mod == 1 else letters[26 - difference]

    else:
        return letters[letter + difference - 1] if mod == 1 else letters[letter - difference - 1]


letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
           'W', 'X', 'Y', 'Z']
