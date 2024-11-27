#Consider a letter representing a hexadecimal #, A = 10, B = 11...
# functions convert b/t a text and encoded value
#       ord('some Char')
#       chr(some number)

# we want hex representation of A, C = 10, 12
ord('A') # = 65
ord('C') # = 67

# convert hex letter its number value
# print(ord('C') - ord('A') + 10)
    # = 67 - 65 = 12


v = 12
unknown = v - 10 + ord('A')
print(unknown)
print(chr(unknown))



# This method will take in a list of #s and return true if it contains 15 consecutive
# #s w/ the same value
#  HELPFUL W METHODS 2(count_runs) & 3(encode_rle)
# def consecutive_fifteen(my_list):
#     count = 1
#     for i in range(len(my_list)-1):
#         if my_list[i] == my_list[i+1]:
#             count+=1
#             if count == 15:
#                 return True
#         else:
#             count = 1
#     return False


# Take in a list of #s & expand them into a larger list. The value in the OG list
#  represents how many times that index (0-indexed) will appear in the new array
# HELPFUL FOR METHOD 5 (decode_rle)
# def expand_by_index(my_list):
#     new_list = []
#     for i in range(len(my_list)):
#         for j in range(my_list[i]):
#             new_list.append(i)
#     return new_list


# Take in a string composed of #s & letters. Return the count of #s in the
# string, ignoring letters
# HELPFUL FOR METHOD 6(string_to_data)
# def numerical_count(string):
#     count = 0
#     for i in string:
#         if i.isdigit():
#             count += 1
#     return count


# def get_hexidecimal_value(c):
#     if c == 'a' or c == 'b' or c == 'c' or c == 'd' or c == 'e' or c == 'f':
#         return ord(c.upper()) - ord('A') + 10
#     else:
#         int_val = ord(c) - ord('0')
#         return int_val
