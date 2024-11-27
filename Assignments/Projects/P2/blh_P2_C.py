from console_gfx import *

welcome = 'Welcome to the RLE image encoder!\n'

spectrum_msg = 'Displaying Spectrum Image: '

menu = '''
RLE Menu
--------
0. Exit
1. Load File
2. Load Test Image
3. Read RLE String
4. Read RLE Hex String
5. Read Data Hex String
6. Display Image
7. Display RLE String
8. Display Hex RLE Data
9. Display Hex Flat Data
'''

selection_prompt = 'Select a Menu Option: '


def decode_rle(my_list):
    new_list = []
    for i in range(len(my_list)):
        if i % 2 == 0:
            for j in range(my_list[i]):
                new_list.append(my_list[i+1])
    return new_list


def begin():
    display_msg(welcome)
    display_msg(spectrum_msg)
    display_image(test_rainbow)
    print()


def display_msg(msg):
    print(msg)


def sum_by_parity(my_list):
    even = 0
    odd = 0
    for i in range(len(my_list)):
        if i % 2 == 0:
            even += my_list[i]
        else:
            odd += my_list[i]
    return [even, odd]


def to_hex_string(data):
    string = ''
    for x in data:
        if x > 9:
            string += chr(ord('a') + (x-10))
        else:
            string += str(x)
    return string


def count_runs(flat_data):
    runs = 1
    count = 1
    for i in range(len(flat_data)-1):
        if flat_data[i] == flat_data[i+1]:
            count += 1
            if count > 15:
                runs += 1
                count = 1
        else:
            runs += 1
            count = 1
    return runs


def encode_rle(flat_data):
    count = 1
    rle_list = []

    for i in range(len(flat_data) - 1):
        if flat_data[i] == flat_data[i + 1]:
            count += 1
            if count > 15:
                rle_list.append(15)
                rle_list.append(flat_data[i])
                count = 1
        else:
            rle_list.append(count)
            rle_list.append(flat_data[i])
            count = 1
    rle_list.append(count)
    rle_list.append(flat_data[-1])

    return rle_list


def get_decoded_length(rle_data):
    sums_by_parity = sum_by_parity(rle_data)
    return sums_by_parity[0]


def string_to_data(data_string):
    new_data = []
    for c in data_string:
        if c.isdigit():
            new_data.append(int(c))
        else:
            c = ord(c.upper()) - ord('A') + 10
            new_data.append(c)
    return new_data


def concat_list_pairs(my_list):
    concat_list  = []
    for i in range(0,len(my_list),2):
        concat_list.append(my_list[i] + my_list[i + 1])
    return concat_list


def to_rle_string(rle_data):
    run_and_hex_list = []

    for i in range(len(rle_data)):
        if i % 2 == 0:
            run_and_hex_list.append(str(rle_data[i]))
        elif rle_data[i] < 10:
            run_and_hex_list.append(str(rle_data[i]))
        else:
            order = rle_data[i] - 10 + ord('A')
            hex_rep = chr(order).lower()
            run_and_hex_list.append(hex_rep)

    run_and_hex_list = concat_list_pairs(run_and_hex_list)
    return ":".join(run_and_hex_list)


def string_to_rle(string):
    output_list = []
    delim_removed_list = string.split(':')

    for hex_num in delim_removed_list:
        a_split = int(hex_num[:-1])
        b_split = int(hex_num[-1], 16)

        output_list.append(a_split)
        output_list.append(b_split)

    return output_list


def main():
    begin()
    image_data = ''
    while True:
        display_msg(menu)
        selection = int(input(selection_prompt))
        if selection == 0:
            break
        elif selection == 1:
            file_name = input("Enter name of file to load: ")
            image_data = load_file(file_name)
        elif selection == 2:
            image_data = test_image
            print("Test image data loaded.")
        elif selection == 3:
            input_data = input('Enter an RLE string to be decoded: ')
            image_data = decode_rle(string_to_rle(input_data))
            print(image_data)
        elif selection == 4:
            input_data = input('Enter the hex string holding RLE data: ')
            image_data = decode_rle(string_to_data(input_data))
            print(image_data)
        elif selection == 5:
            input_data = input('Enter the hex string holding flat data: ')
            image_data = string_to_data(input_data)
            print(image_data)
        elif selection == 6:
            print("Displaying image...")
            if image_data:
                display_image(image_data)
            else:
                print('(no data)')
        elif selection == 7:
            if image_data:
                rle_string = to_rle_string(encode_rle(image_data))
            else:
                rle_string = '(no data)'
            print(f"RLE representation: {rle_string}")
        elif selection == 8:
            if image_data:
                rle_hex = to_hex_string(encode_rle(image_data))
            else:
                rle_hex = '(no data)'
            print(f"RLE hex values: {rle_hex}")
        elif selection == 9:
            if image_data:
                flat_hex = to_hex_string(image_data)
            else:
                flat_hex = '(no data)'
            print(f"Flat hex values: {flat_hex}")
        else:
            print('Error! Invalid input.')


if __name__ == '__main__':
    main()



























