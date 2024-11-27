# my = [22,33,44,55,66,78]
# even_sum = 0
#
# for i in my:
#     if i % 2 == 0:
#         even_sum +=i
#
# print(even_sum)

# l1 = [1,2,3,67,7]
# l2 = [3,9,8,2,7]
#
# common = [i for i in l1 if i in l2]
# print(common)

# l3 = ['oranges','apples','kiwi']
#
# len5 = [i for i in l3 if len(i) >= 5]
# print(len5)

# c = [4,1,3,6]
# c[0:-1] = '12'
# print(c)
# c = ['1', '2', 6]

# a = [8] *2
# a[:] = [6]
# print(a)

# t1 = 1,
# t2 = 3,4,5
# t3 = t1+t2
# print(t3)
#
# a,*d = t3
# print(a,d)
# d = 1 [3, 4, 5]

# l = [1,2,3,4,5]
# for index,item in enumerate(l):
#     print(f'Index {index}: {item}')

# dict = {'item': 'one', 'val': 2, 3: ['a','b']}
#
# dict.get('items')

# a = {1,2,3,4}
# b = set([4,5,6])
# c = a.union(b)
# d = a.intersection(b)
# e = a.difference(b)
# print(e)

# a,b = 11,11
# c,d = 'hello', 'hello'
#
# e = [1,2,4]
# f = [1,2,4]
# print(e == f)

# a = [2, (7, 'Joe'), 6]
# a[0:1] = [2]
#
# a = {2,3,4,5}
# b = {3,4,5,8}
# c = a.union(b)
# print(c[1:3])

# def print_triangLe(base):
#     for i in range(base):
#         for j in range(i+1):
#             print('*', end=' ')
#         print()
#
# print_triangLe(4)

# def print_tri_rev(base):
#     for i in range(base,0,-1):
#         for j in range(i,0,-1):
#             print("*", end=' ')
#         print()
# print_tri_rev(4)

#prime number = number greater than 1, only divisible by 1 & itself.
# Write a method is_prime(n)to detect whether a number is prime or not.

# def is_prime(n):
#     for i in range(2,n//2+1):
#         if n % i == 0:
#             return False
#     return True
#
# print(is_prime(18))


# def largest_sublist(list,sum):



ist = [1,2,3]
for i in range(len(ist)):
    print(ist[i])

