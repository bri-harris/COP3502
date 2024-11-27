# x = 5
# y = 6

# print("yes") if x == y else print("No") 

# a = 51
# b =- 72
# print(a) if a>b else print(b)
# i = 1
# while(i<=10):
#     print(i, end = " ")
#     i+=1

# write a program to calculate the factorial of a given number
given = float(input("Provide number to calulate the Factorial:    "))
loop_var = given
while(loop_var>1):
    given *= (loop_var - 1)
    loop_var -=1
print(given)