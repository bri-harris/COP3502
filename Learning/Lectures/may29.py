# str = 'python'
# for i in str:
#     print(i)

# use a for loop to generate a factorial for a given number

# num = int(input("Input a number: "))
# for i in range(1,num):
#     num *= i
# print(num)

# x = 5
# for i in range(1,5,3):
#     x+=10
# print(x)

# generate pattern to take user input and generate a matrix of * = to input
# **
# **
# l = int(input("Enter a length: "))
# for i in range(1,l+1):
#     for j in range(1,l+1):
#         print("*", end="")
#     print()

# generate pattern to take user input and generate a right triangle of * w base = input
# *
# **
# ***
# b = int(input("Enter a base: "))
# for i in range(1,b+1):
#     for j in range(1,i+1):
#         print("*", end='')
#     print()

# generate pattern to take user input and generate a right triangle of * w TOP base = input
# ***
# **
# *
b = int(input("Enter a base: "))
for i in range(1,b+1):
    for j in range(1,b+2-i):
        print('*', end = '')
        break
    print()