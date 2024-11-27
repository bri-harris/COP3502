var ='CHAPTER 3 LISTS'

# pals = ["Maddy", "emily","kylie"]
# print(pals)
# print(pals[1].title())

# print(f"Happy aniversary {pals[0]}")
# print(f"Hey {pals[-1].title()} I hope we can make up")

# pals.insert(1,"name")

# dinner_list = ['RBG', 'Sara Bareilles', 'Gloria Stinem']
# # for i in dinner_list:
# #     print(f"{i}, would you like to come to dinner?")

# print(f"{dinner_list.pop(0)} can't make dinner.")
# dinner_list.insert(0,"Obama")
# # print(f"I'll have to send out an invite to {dinner_list[0]}")   
# print("We found a bigger table, we'll invite a few more people..")

# dinner_list.insert(0,'elton john')
# dinner_list.insert(2,'Jodie comer')
# dinner_list.append('Christopher')

# # for i in dinner_list:
# #     print(f"{i.title()}, would you like to come to dinner?")
# print("The table wont come in time, original invitees only.")

# for i in range(5,1,-1):
#     print(f"I'm sorry {dinner_list.pop(i)}, we'll have to rescedule")

# for i in dinner_list:
#     print(f"I'm looking forward to dinner {i}!")
    
# del dinner_list[0]
# del dinner_list[0]
# print(dinner_list)

# SORTING LISTs
cars = ['bmw', 'audi', 'toyota', 'suburu']

# # cars.sort(reverse=True)
# cars.sorted()
# len(cars)
# locations = ['croatia','spain','italy','greece','hawaii']
# print(locations,": original list")
# print()

# print(sorted(locations),": Temp sorted")
# print(sorted(locations,reverse=True),": Temp reversed sorted")
# print()

# locations.reverse()
# print(locations,": permanant, reversed list")
# print()

# locations.reverse()
# print(locations,": back to original, reversed list permanant")
# print()

# locations.sort()
# print(locations, ":Alphabetical sort, permanent")

# locations.sort(reverse=True)
# print(locations, ":Reverse alphabetical sort, permanent")

# print(len(locations), ": length of locations list")



var = 'CHAPTER 4 WORKING W LISTS'

pizzas = ['cheese','pepperoni','pineapple']
# for pizza in pizzas:
#     print("I know about", pizza, "pizza.")
# print("Those were the first pizzas I could think of...")

# pets= ['fish','lizard','frog']
# for pet in pets:
#     print(pet, 'is a cool pet.')
# print("In fact these are all pets I've owned!")
# numbers = list(range(1,6))
# print(numbers)
# min(numbers)
# max(numbers)
# print(sum(numbers))

# squares = []
# for value in range(1,11):
#     squares.append(value**2)

# squares = [value**2 for value in range(1,11)]
# print(squares)

# numbers = [value+1 for value in range(1_000_000)]
# # print(numbers)
# print(min(numbers))
# print(max(numbers))
# print(sum(numbers))

# three_numbers = list(range(3,31,3))
# for three in three_numbers:
#     print(three)

# cubed = [value**3 for value in range(1,10)]
# print(cubed)

# print("The first 3 cubed numbers are:",cubed[0:3])
# print("The next 3 cubed numbers are:",cubed[3:6])
# print("The last 3 cubed numbers are:",cubed[6:])

# copied_pizzas = pizzas[:]
# pizzas.append('Veggie')
# copied_pizzas.append('White sauce')
# print(pizzas)
# print(copied_pizzas)

# immutable_list = ('chicken','fries','potatoes','burrito','beer')
# for item in immutable_list:
#     print(item)

# # immutable_list[0] = 'steak' ERROR


# revised_menu = ('steak','brocoli','potatoes','burrito','beer')
# for item in revised_menu:
#     print(item)

print('audi' not in cars)