# try:
#     a,b = 0,1
#     if a == 0:
#         raise ValueError('Invalid, a = 0')
#     print('result', a/b)
# except ZeroDivisionError as e:
#     print(str(e))
# except ValueError as e:
#     print("Caught ValueError:", str(e))
# except:
#     print('Something went wrong')

def calc_avg(nums):
    total = sum(nums)
    return total / len(nums)

