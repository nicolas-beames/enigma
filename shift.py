def shift(amount):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    chars = []
    temp = []
    for i in alphabet:
        chars.append(i[:1])
        temp.append(i[:1])

    for i in chars:
        if chars.index(i) + amount < 26:
            temp[chars.index(i)] = chars[chars.index(i) + amount]
        else:
            temp[chars.index(i)] = chars[(chars.index(i) + amount) - 26]
    chars = temp

    return chars
