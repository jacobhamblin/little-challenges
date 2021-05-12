def decode(str):
    if not str or len(str) < 2:
        return 1
    if len(str) >= 2 and int(str[0:2]) > 9 and int(str[0:2]) < 27:
        return 1 + decode(str[1 : len(str)])
    return decode(str[1 : len(str)])
