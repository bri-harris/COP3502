# x = 15
# if x % 3 ==0:
#     print('Yes')
# else:
#     print('No')
# if x % 5 ==0:
#     print('Yes')
# else:
#     print('No')


# if x %3 ==0:
#     print('Yes')
# else:
#     if x % 5 == 0:
#         print("Yes") 
#     else:
#         print("No")

# if x %3 ==0:
#     print('A')
#     if x % 5 != 0:
#         print("C")
#     else:
#         print('B')
# else:
#     print("D")

# if x %3 !=0:
#     print('A')
# else:
#     if x % 5 == 0:
#         print("C")
#     else:
#         print('B')
#     print('D')

# x,y = 32,38

# if x>= 0 and x<= y:
#     if x<=100 or y> 50:
#         x= x //10
#         if y<50:
#             x +=1
#         y = y-1
#     else:
#         y-= 1
# else:
#     y-=x

# print(x+y)

#user inputs any given year, write a program to determine if the given year is a leap year or not

year = input("Input any year: ")
if float(year) % 4 == 0:
    if float(year) % 100:
        if float(year) % 400:
            print(year +' is a leap year')
    else:
        print(year + ' is not a leap year')
else:
    print(year + ' is not a leap year')