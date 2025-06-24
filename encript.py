from shift import shift


def encript(msg):
    rotors = {'A': 5, 'B': 7, 'C': 10}

    for key, value in rotors.items():
        print(f'Rotor={key}, shift={shift(value)}')

    return "a"