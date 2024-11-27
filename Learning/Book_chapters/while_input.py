# choice = input("What kind of car would you like?")
# print(f"Cool, let me see if I can find you a {choice}")

# num = input("How many people are in your party?")
# if int(num)> 8:
#     print("There will be a wait")
# else:
#     print("Follow me to your table")

# num = int(input("Give me a number"))

# if num % 10 == 0:
#     print(f"{num} is a multiple of 10!")
# else:
#     print(f"remainder: {num % 10}")


# while True:
#     topping = input("name a topping to add: ")
#     if topping.lower() == 'quit':
#         break
#     print(f"Adding {topping} to your order")

# while True:
#     prompt = input("How old are you?")
#     if prompt == 'quit':
#         break
#     else:
#         age = int(prompt)
#         if age <3:
#             print("Ticket is free")
#         elif age < 12:
#             print("Ticket is $10")
#         else:
#             print("Ticket price is $15")

sandwhich_orders = ['meatball sub','pb & j','pastrami', 'chopped cheese', 'tuna melt','pastrami','pastrami']
finished_sandwhiches = []

print('We are all out of Pastrami!')
while 'pastrami' in sandwhich_orders:
    sandwhich_orders.remove('pastrami')

while sandwhich_orders:
    order = sandwhich_orders.pop()
    print(f"order up {order}!!!")
    finished_sandwhiches.append(order)
print("All orders have been completed")
print(finished_sandwhiches)