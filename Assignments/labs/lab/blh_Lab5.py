menu = '''Decoding Menu
-------------
1. Decode hexadecimal
2. Decode binary
3. Convert binary to hexadecimal
4. Quit

Please enter an option: '''


def hex_char_decode(hex):
    value_store = {
        '0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8,
        '9': 9, 'a': 10, 'b': 11, 'c': 12, 'd': 13, 'e': 14, 'f': 15
    }

    hex = hex.lower()
    return value_store[hex]


def hex_string_decode(digit):
    if digit[:2] == '0x':
        digit = digit[2:]

    decimal = 0
    power = len(digit) - 1
    digit = digit.lower()

    for char in digit:
        decimal += hex_char_decode(char) * (16 ** power)
        power -= 1
    return decimal


def binary_string_decode(binary):
    if binary[:2] == '0b':
        binary = binary[2:]

    decimal = 0
    power = len(binary) - 1

    for char in binary:
        if char == '0':
            char = 0
        else:
            char = 1
        decimal += char  * (2 ** power)
        power -= 1

    return decimal


def binary_to_hex(binary):
    value_store = {
        0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8',
        9: '9', 10: "a", 11: "b", 12: "c", 13: "d", 14: "e", 15: "f"
    }

    decimal = binary_string_decode(binary)
    str = ''
    q = decimal // 16
    r = decimal % 16

    while q > 0:
        str = value_store[r] + str
        r = q % 16
        q //= 16

    return (value_store[r] + str).upper()


def in_and_out(f):
    s = input('Please enter the numeric string to convert: ')
    print('Result:', f(s))
    print()


def main():
    while True:
        selection = int(input(menu))
        if selection == 1:
            in_and_out(hex_string_decode)
        elif selection == 2:
            in_and_out(binary_string_decode)
        elif selection == 3:
            in_and_out(binary_to_hex)
        elif selection == 4:
            print('Goodbye')
            print('!')
            break


if __name__ == '__main__':
    main()