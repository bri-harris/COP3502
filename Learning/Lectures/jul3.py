# from datetime import date
#
#
# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     @classmethod
#     def from_birth_year(cls, name, year):
#         print(cls)
#         return cls(name, date.today().year - year)
#
#     @staticmethod
#     def is_adult(age):
#         return age > 18
#
#
# a = Person('kay', 26)
# b = Person.from_birth_year('bri', 1998)

# class Monster:
#     def __init__(self, level=1, name='Monster'):
#         self.level = level
#         self.name = name
#
#     def __str__(self):
#         return self.name + \
#             " lvl " + \
#             str(self.level)
#
#     def __eq__(self, other):
#         if isinstance(other, Monster):
#             return self.level == other.level \
#                 and self.name == other.name
#
#     def __lt__(self, other):
#         if isinstance(other, Monster):
#             return self.level < other.level
#
#     def __repr__(self):
#         return f"{self.name} lvl {self.level}"
#
#
# a = Monster(50, 'Alakazam')
# t = Monster(55, 'Tyranitar')
# b = Monster(8, 'Bulbasaur')
#
# pokemon = [a, t, b]
# pokemon.sort()
# print(pokemon)
#
# pokemon.sort(key=lambda mon: mon.name)
# print(pokemon)

# class Person:
#     def __init__(self,name,age=18):
#         self.name = name
#         self.age = age
#
#     def age_change(self,new_age):
#         self.age = new_age
#
# p1 = Person('bri',26)
#
# p1.job = 'Engineer'
#
#
# class Student:
#     pass
#
# s1 = Student()

# class Circle:
#     pi = 3.14
#
#     def __init__(self, radius):
#         self.radius = radius
#
#     def area(self):
#         return self.pi * self.radius * 2
#         #  OR self.pi
#
#
# c = Circle(1)
# c.pi = 3.1415

#
class Employee:
    def __init__(self, first, last):
        self.first = first
        self.last = last

    @property
    def fullname(self):
        return f"{self.first} {self.last}"

    @fullname.setter
    def fullname(self,name):
        self.first, self.last = name.split()

emp = Employee('Tom','Smith')
emp.fullname = 'Jose Adam'
print(emp.fullname)


# class Account:
#     def __init__(self, balance=0):
#         self.balance = balance
#
#     def deposit(self,amount):
#         self.balance += amount
#
#     def withdraw(self, amount):
#         if self.balance >= amount:
#             self.balance -= amount
#
#
# class SavingsAccount(Account):
#     def __init__(self,balance,rate):
#         Account.__init__(self,balance)
#         self.interest_rate = rate
#
#     def add_interest(self):
#         interest = self.balance * self.interest_rate
#         Account.deposit(self,interest)
#
#
# class CheckingAccount(Account):
#     transaction_fees = 3
#     free_transactions = 4
#
#     def __init__(self,balance):
#         self.transaction_count = 0
#         super().__init__(balance)
#
#     def deposit(self,amount):
#         self.transaction_count += 1
#         super().deposit(amount)
#
#     def withdraw(self, amount):
#         self.transaction_count += 1
#         Account.withdraw(self,amount)
#
#
# sh = SavingsAccount(100,.02)
# ch = CheckingAccount(300)
# sh.deposit(20)
# ch.deposit(20)

# class Account:
#     interest = .01
#
#     def __init__(self, holder, balance=0):
#         self.holder = holder
#         self.balance = balance
#
#     def deposit(self, amount):
#         self.balance += amount
#
#     def withdraw(self, amount):
#         if self.balance >= amount:
#             self.balance -= amount
#
#
# class CheckingAccount(Account):
#     interest = .02
#     withdraw_fee = 1
#
#     def withdraw(self, amount):
#         return Account.withdraw(self, amount + self.withdraw_fee)
#
#
# class Bank:
#     def __init__(self):
#         self.accounts = []
#
#     def open_account(self, holder, amount, kind=Account):
#         account = kind(holder, amount)
#         self.accounts.append(account)
#         return account
#
#     def pay_interest(self):
#         for acc in self.accounts:
#             acc.deposit(acc.balance * acc.interest)
#
#
# bank = Bank()
# sally = bank.open_account('sally', 100)
# tom = bank.open_account('tom', 300, CheckingAccount)
# print(sally.interest, tom.interest)
# bank.pay_interest()
# print(sally.balance, tom.balance)
