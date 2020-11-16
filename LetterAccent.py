def remove(letter):

    if letter in ('á', 'ã', 'â', 'Á', 'Ã', 'Â'):
        return "A" if letter.isupper() else "a"
    elif letter in ('é', 'ê', 'É', 'Ê'):
        return "E" if letter.isupper() else "e"
    elif letter in ('í', 'î', 'Í', 'Î'):
        return "I" if letter.isupper() else "i"
    elif letter in ('ó', 'õ', 'ô', 'Ó', 'Õ', 'Ô'):
        return "O" if letter.isupper() else "o"
    elif letter in ('ú', 'û', 'Ú', 'Û'):
        return "U" if letter.isupper() else "u"
    elif letter in ('ç', 'Ç',):
        return "C" if letter.isupper() else "c"
    else:
        return letter
