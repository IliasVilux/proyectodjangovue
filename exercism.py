COLORS = {
    'black': 0,
    'brown': 1,
    'red': 2,
    'orange': 3,
    'yellow': 4,
    'green': 5,
    'blue': 6,
    'violet': 7,
    'grey': 8,
    'white': 9
}

OHMS = {
    'ohms': 1e3,
    'kiloohms': 1e6,
    'megaohms': 1e9,
    'gigaohms': 1e12
}


def label(colors: [str, str, str]) -> str:
    prefix = ''.join([str(COLORS[color]) for color in colors][:2])

    if (prefix == '00'):
        return '0 ohms'
    
    prefix += '0' * COLORS[colors[2]]

    previous_value = ''
    for key, value in OHMS.items():
        if int(prefix) < value:
            if previous_value != '':
                return f'{round(int(prefix)/OHMS[previous_value])} {key}'
            else:
                return f'{round(int(prefix))} {key}'
        previous_value = key

print(label(["orange", "orange", "black"]))