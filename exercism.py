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
    'ohms': 1,
    'kiloohms': 1e6,
    'megaohms': 1e9,
    'gigaohms': 1e12
}


def label(colors: [str, str, str]) -> str:
    prefix = ''.join([str(COLORS[color]) for color in colors][:2])

    if (prefix == '00'):
        return '0 ohms'
    
    prefix += ''.join(['0' for _ in range(COLORS[colors[2]])])
    return ''.join(str(value) for value in OHMS.values() if round(int(prefix)) < value)
    # return next(f'{round(int(prefix) / exp)} {unit}' for unit, exp in OHMS.items() if int(prefix) < exp)

    # prefix_numeric = int(prefix)
    # if prefix_numeric < 1e3:
    #     return f'{round(prefix_numeric)} ohms'
    # elif prefix_numeric < 1e6:
    #     return f'{round(prefix_numeric/1e3)} kiloohms'
    # elif prefix_numeric < 1e9:
    #     return f'{round(prefix_numeric/1e6)} megaohms'
    # elif prefix_numeric < 1e12:
    #     return f'{round(prefix_numeric/1e9)} gigaohms'

print(label(["white", "white", "white"]))