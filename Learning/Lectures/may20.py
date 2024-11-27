# objects
# name = input("Enter your name: ")
# print(name)

# print(type(name))
# print(id(name))

# print("Hello", "World", sep="-",end="!")
# print("Python is fun.")


# Decision Making and conditionals
# total = float(input("Enter the total: "))

# if total > 90:
#     print("Satisfactory performance!")
# elif total >80:
#     print("B Grade")
# else:
#     print("Non-Satisfactory.")

# Write a program to calculate the final price paid if the store has a deal, 'buy 3, pay for the most expensive item'

c1 = float(input("Enter c1: "))
c2 = float(input("Enter c2: "))
c3 = float(input("Enter c3: "))
if c1>c2 and c1 > c3:
    print("c1 is the costliest at price: ",c1)
elif c2>c1 and c2>c3:
    print("c2 is the costliest at price: ",c2)
else:
    print("c3 is the costliest at price: " ,c3)