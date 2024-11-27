# Fibanocci Sequence Function
def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n-1) + fibonacci(n-2)
# print((fibonacci(5)))

# Efficient Memorization Technique for Fibonacci Sequence function
# store calculated values in a dictionary reducing computation requirements
def fib(n,d):
    if n in d:
        return d[n]
    if n == 0 or n == 1:
        return n

    d[n] = fib(n-1,d) + fib(n-1,d)
    return d[n]


# example 1
def recursive_sum(n):
    if n == 0:
        return 0
    else:
        return n + recursive_sum(n-1)
# print(recursive_sum(5))


# Design a recursive function that writes positive numbers to the screen w/ the digits written
# vertically. so 1234 =
# 1
# 2
# 3
# 4
def pd(n):
    if n<10:
        print(n)
        return

    pd(n // 10)
    print(n%10)


# Example 2
def mystery(b,e):
    if e == 0:
        return 1
    else:
        return b * mystery(b,e-1)


# Example 3
def magic(n):
    if n <10:
        return n
    return magic(n //10) + n % 10


# Factorial of a number
def fact(n):
    if n == 1:
        return n
    return fact(n-1) * n


# Recursive String Palindrome
def pal(n):
    if len(n) <= 2 and n[0] == n[-1]:
        return True
    if n[0] == n[-1]:
        return pal(n[1:-1])
    return False



# Recursion with Efficiency Example
def mag(arr,size,target):
    if size == 0:
        return 0

    if arr[size -1] == target:
        return 1 + mag(arr,size - 1, target)
    return mag(arr,size - 1, target)

arr = [3,4,1,4,5,12,4]
target = 4
print(mag(arr,len(arr),target))