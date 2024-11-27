from car import Car as C
import electric_car as EC

my_mustang = C('Ford', 'mustang', 2024)
print(my_mustang.get_descriptive_name())

my_leaf = EC.ElectricCar('nissan', 'leaf', 2024)
print(my_leaf.get_descriptive_name())

# from car import *
#
# eb = ElectricCar('a','b',1)

# import car
#
# my_mustang = car.Car('Ford', 'mustang', 2024)
# print(my_mustang.get_descriptive_name())

# from car import Car
# from car import ElectricCar
# from car import Battery
#
#
# my_new_car = Car('audi', 'a4', 2023)
# print(my_new_car.get_descriptive_name())
# my_new_car.odometer = 23
# my_new_car.read_odometer()
#
# my_mustang = Car('Ford', 'mustang', 2024)
# print(my_mustang.get_descriptive_name())
#
# my_leaf = ElectricCar('nissan', 'leaf', 2024)
# print(my_leaf.get_descriptive_name())
'''
issues with mobile log in flow. We are seeing CORS errors when trying to load the iframe:
xerxes iframe error:  DOMException: Failed to read a named property 'hash' from 'Location': Blocked a frame with origin "https://local.tv.xfinity.com" from accessing a cross-origin frame.
    at IframeRedirect._onLoad
Previously we were using prompt=none for logging in but after some discussions we were advised to omit this parameter since id_token_hint was required when passing prompt=none
'''
