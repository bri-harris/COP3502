class Dog:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def sit(self):
        print(f"{self.name}, sit!")

    def roll_over(self):
        print(f"{self.name}, roll over!")

# d1 = Dog('Rex',15)
# print(f"{d1.name} is {d1.age} years old")
# d1.roll_over()
# d1.sit()

class Restaurant:
    def __init__(self, name, cruisine, num_served = 0):
        self.name = name
        self.cruisine = cruisine
        self.num_served = num_served

    def describe(self):
        print(f"{self.name} offers {self.cruisine}, and has served {self.num_served} patrons")

    def open(self):
        print("We're open!")

    def serve_patrons(self,num):
        self.num_served += num

    def set_patron_served(self,patrons):
        self.num_served = patrons


class IceCreamStand(Restaurant):
    def __init__(self,name,cruisine,num_served,flavors):
        super().__init__(name,cruisine,num_served)
        self.flavors = flavors

    def display_flavors(self):
        print("We offer the following: ")
        for flavor in self.flavors:
            print(flavor.title())

# ralphs = IceCreamStand('ralphs','Icecream',10,['vanilla','chocolate','strawberry'])
# ralphs.display_flavors()
# nauti = Restaurant('Nauti Spirits','Cocktails')
# nauti.describe()
# nauti.open()
# nauti.serve_patrons(24)
# print(nauti.num_served)
# nauti.set_patron_served(14)
# print(nauti.num_served)


class Privileges:
    def __init__(self,privileges = ['Read']):
        self.privileges = privileges

    def show_privileges(self):
        print(f"Users privileges include", end=' ')
        for ability in self.privileges:
            print(f"'{ability}'",end=' ')


class Users:
    def __init__(self, first,last):
        self.first = first
        self.last = last
        self.privileges = Privileges()

    def describe(self):
        print(f"User {self.first.title()} {self.last.title()}",end=' ')


u1 = Users('dinko','mitic')
admin_rights = Privileges(['Read','Write','Execute'])
u1.privileges = admin_rights
u1.privileges.show_privileges()















