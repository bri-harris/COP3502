# def fibonacci(n):
#     if n == 1 or n == 2:
#         return 1
#     return fibonacci(n-1) + fibonacci(n - 2)

# def factorial(n):
#     if n == 1:
#         return 1
#     elif n == 2:
#         return 2
#     return n * factorial(n - 1)

# def sum_to(n):
#     if n == 1:
#         return 1
#     return n + sum_to(n - 1)

# class Employee:
#     def __init__(self,name,employee_id,salary):
#         self.name = name
#         self.employee_id = employee_id
#         self.salary = salary
#
#     def display_info(self):
#         print(f'Name: {self.name}, ID: {self.employee_id}, \nsalary: {self.salary}')
#
#     def update_salary(self, new_salary):
#         self.salary = new_salary
#
# class Manager(Employee):
#     def __init__(self,name,employee_id,salary,department):
#         super().__init__(name,employee_id,salary)
#         self.department = department
#
#     def display_info(self):
#         super().display_info()
#         print(f'department: {self.department}')

# b = Employee('bri',8703,139000)
# b.display_info()
# b.update_salary(2000000)
# b.display_info()

# c = Manager('Christina',99,2000000,'Engineering')
# c.display_info()


# class Vehicle:
#     def __init__(self,make,model,year):
#         self.make = make
#         self.model = model
#         self.year = year
#
#     def display_info(self):
#         print(f'Make {self.make}')
#         print(f'Model {self.model}')
#         print(f'Year {self.year}')
#
#
# class Car(Vehicle):
#     def __init__(self,make,model,year,num_doors):
#         super().__init__(make,model,year)
#         self.num_doors  = num_doors
#
#     def display_info(self):
#         super().display_info()
#         print(f'Doors {self.num_doors}')
#
#
# class Motorcycle(Vehicle):
#     def __init__(self,make,model,year,has_sidecar):
#         super().__init__(make,model,year)
#         self.has_sidecar = has_sidecar
#
#     def display_info(self):
#         super().display_info()
#         print(f'Sidecar: {self.has_sidecar}')


# def l_nums(l):
#     assert len(l)>2, 'List must have at least 3 elements'
#     for i in range(len(l)):
#         print(f'{i}: {l[i]}',end=', ')


# def int_convert():
#     while True:
#         try:
#             user_input = int(input('Input an Int to be converted: '))
#             return user_input
#         except ValueError as e:
#             print(str(e))
#             print('Error, non-numeric value')
#         except:
#             print('Something went wrong')


# class DivisionByTwo(Exception):
#     pass
#
# def divide(a, b):
#     if b == 2:
#         raise DivisionByTwoError('Cannot divide by two')
#     return a / b
#
# try:
#     print(divide(10,5))
#     print(divide(10,2))
# except DivisionByTwoError as e:
#     print(f"Error: {e}")

def calculate_area(l,w):
    return l * w