# def calc_square_root(num):
#     assert num >= 0, "Cannot calculate square root of a negative number."
#     return num **.5
#
# try:
#     result1 = calc_square_root(16)
#     print(f"Square root of 16 is: {result1}")
#     result2 = calc_square_root(-9)
#     print(f"Square root of -9 is: {result2}")
# except AssertionError as e:
#     print(str(e))

# def divide_numbers(a,b):
#     assert b != 0, "Cannot divide by Zero"
#     return a/b
#
#
# def test_divide_numbers():
#     try:
#         result = divide_numbers(10,2)
#         assert result == 5
#         print("Test case 1 passed")
#
#         result = divide_numbers(10,0)
#         assert result == float('inf')
#         print("Test case 2 passed")
#     except AssertionError as e:
#         print(f"Test case failed: {str(e)}")
#
# test_divide_numbers()
#
# print("Welcome to assertions and exceptions")
# arr = []
# try:
#     num = int('two')
#     if num < 0:
#         raise ValueError("555")
#     arr[num] = 6
#     print(arr)
#     num = num / 0
#     print(num)
# except ZeroDivisionError as err:
#     print("101")
# except ValueError as err:
#     print("010")
#     print(str(err))
# except Exception as err:
#     print(str(err))
# finally:
#     print("123")

# try:
#     rand_dic = {'a': [2, 5, 4, 9], 'b': 'happy face', 'c': 2, 'd': {4,5,6}}
#     rand_dic['c'] += 3
#     rand_dic['d'] .add(4)
#     print(rand_dic['a'][5])
# except KeyError:
#     print('Key Error')
# except IndexError:
#     print('index OOR')
# except:
#     print('Something went wrong')
# print(rand_dic.pop('e'))

country_capitals = {"Lebanon": "Beirut", "Bangladesh": "Dhaka", "Guyana": "Georgetown"}
capitals = [cap for cap in country_capitals.values()]
print(capitals)