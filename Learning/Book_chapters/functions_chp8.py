# def greet(name):
#     print(f"Hello {name}")
    
# greet('Bri')
# hello = greet
# hello('Maddy')
# def display_message():
#     print("This chapter introduces functions")
    
# def favorite_book(title):
#     print(f"{title.title()} is a great book choice!")
    
# display_message()
# favorite_book('The Alchemist')

# def make_shirt(text, size='Large'):
#     print(f"Size: {size}\nMessage: {text}")
    
# make_shirt('Go Gators!')

# def city_country(city,country):
#     cc = f"{city}, {country}"
#     return cc.title()


# print(city_country('new york', 'united states'))

# def make_album(artist, album):
#     album = {'artist': artist, 'album': album}
#     return album


# i = 0
# while i <3:
#     print('Lets build an album!')
#     art = input('Whos the artist?\t')
#     al = input("What album should we document?\t")
#     print(make_album(art,al))
#     print()
#     i+=1

# messages = ['Morning', 'Afternoon','Evening']
# sent_messages = []

# def show_message(messages):
#     for message in messages:
#         [print(f"Good {message}.")]
        
# # show_message(messages)

# def send_message(messages, sent_messages):
#     while messages:
#         send = messages.pop()
#         print(f"Good {send}")
#         sent_messages.append(send)

# send_message(messages[:],sent_messages)
# print(messages)
# print(sent_messages)

# def name_tuple(*names):
#     print(names)
    
# name_tuple('bri','maddy','kayla','abby')

# def person(first,last,**info):
#     info['first_name'] = first
#     info['last_name'] = last
#     return info

# person_data = person('bri','har',field='CS',city='NYC')
# print(person_data)

# def sandwhich_toppings(*toppings):
#     print("Sandwhich order with: ")
#     for top in toppings:
#         print(f"\t- {top}")
        
# sandwhich_toppings('ham','cheese','mayo')


# def car_dictionary(manufacturer, model, **car):
#     car['manufacturer'] = manufacturer
#     car['model']=model
#     return car

# car_1 = car_dictionary('Jeep', 'Wrangler', full_wd=True,doors=2)
# print(car_1)

# def sq(x):
#     return x*x

# def sum_sq(n):
#     total = 0
#     for i in range(n+1):
#         square = lambda x: x*x
#         total+=square(i)
#     return total

# print(sum_sq(4))

# sum = lambda x,y: x+y
# print(sum(1,2))

# def f_name(func,y,z):
#     text = func(y,z)
#     print(text)

# def format(a,b):
#     return a+b

# f_name(format,'bri','har')

# def add(x,y):
#     return x+y

# print(add(3,9))
# print(add('hello','world'))

# a,b = 2,3

# def hey():
#     global a
#     a = 'two'
#     b = 'three'
    
# print(a,b)
# hey()
# print(a,b)

# def plus(x):
#     x=x+1

# y = 8
# plus(y)
# print(y)

def scop(z,a_list):
    z+=4
    a_list[1] = 4
    a_list = [100,102]

x=2
nums = [6,9,12]
scop(x,nums)
print(x,nums)