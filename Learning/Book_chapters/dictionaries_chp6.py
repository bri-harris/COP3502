# dict = {'item': 'one', 'val': 2, 3: ['a','b']}
# print(dict[3])

# dict['day'] = 'Monday'
# del dict['day']

# print(dict)

# get_method = dict.get(4,"There isnt a 4th item yet")
# print(get_method)
# print(dict)

# maddy = {'eyes': 'Green/Hazel', 'hair': 'blonde','cute':'yes'}
# for k,v in maddy.items():
#     print(F"\nKey: {k}")
#     print(F"Value: {v}")

# for k in sorted(maddy.keys()):
#     print(k)
    
# languages = {'bri': 'Java', 'bapuji': 'Java', 'Saranya':'Java', 'Dinko': 'Python'}
# for lang in set(languages.values()):
#     print(lang)

# rivers = {'Magothy': 'USA', 'Severn': 'USA', 'Nile': 'Egypt'}

# for k,v in rivers.items():
#     print(f"The {k} runs in {v}.")

# for k in rivers:
#     print(k)

# for country in set(rivers.values()):
#     print(country)

# fav_lang = {
#     'jen': 'python',
#     'sarah': 'c',
#     'edward': 'rust',
#     'phil': 'python'
# }

# people = ['Bapuji','Dinko','phil','sarah']

# for ppl in people:
#     if ppl in fav_lang:
#         print(f"Thanks {ppl} for responding to the poll!")
#     else:
#         print(f"\t{ppl}, whats your favorite language?")        

# aliens = []

# for alien in range(30):
#     new_alien = {'color':'green','points':5,'speed':'slow'}
#     aliens.append(new_alien)

# for alien in aliens[:5]:
#     print(alien)
# print(f"There are {len(aliens)} aliens.")

# print()

# for alien in aliens[:3]:
#     if alien['color'] == 'green':
#         alien['color'] = 'yellow'
#         alien['speed'] = 'medium'
#         alien['points'] = 10
        
# for alien in aliens[:5]:
#     print(alien)

# pizza = {
#     'crust': 'regular',
#     'toppings': ['mushrooms','extra cheese']
# }

# print(f"Pizza with {pizza['crust']} crust and the following toppings:")
# for top in pizza['toppings']:
#     print(top)

# fav_lang = {
#     'jen': ['python','rust'],
#     'sarah': ['c'],
#     'edward': ['rust','go'],
#     'phil': ['python','haskell']
# }

# for key in fav_lang:
#     print(f"{key.title()}'s favorite languages are:")
#     for langs in fav_lang[key]:
#         print(f"\t{langs}")

# users={
#     'bri_harris':{
#         'first': 'Bri',
#         'last':"Harris",
#         'location': 'chelsea'
#     },
#     'mmiller':{
#         'first': 'Maddy',
#         'last':'Miller',
#         'location': 'bk'
#     }
# }

# for user_name, user_information in users.items():
#     print(f"Username: {user_name}")
#     print(f"\tFull name: {user_information['first']} {user_information['last']}")
#     print(f"\tLocation: {user_information['location']}")