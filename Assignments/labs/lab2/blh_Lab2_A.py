s_1 = float(input("Side length 1: "))
s_2 = float(input("Side length 2: "))
s_3 = float(input("Side length 3: "))

if s_1 == s_2 and s_1 == s_3:
    print("This is an equilateral triangle!")
elif s_1 == s_2 or s_2 == s_3 or s_3 == s_1:
    print("This is an isosceles triangle!")
else:
    print("This is a scalene triangle!")
    