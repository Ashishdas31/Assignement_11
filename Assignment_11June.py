# Ans.  6.
square = lambda x: x**2

N = 5
Result = square(5)
print(Result)

# Ans.  7.

Integer_List = [10, 50, 20, 60, 100, 95]


number = lambda lst: max(lst)

Result1 = number(Integer_List)
print(Result1)

# Ans.  8.
number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

Even = list(filter(lambda x: x % 2 == 0, number_list))

print(Even)

# Ans.  9.
strings = ["apple", "banana", "cherry", "date", "elderberry"]

sorted_strings = sorted(strings, key=lambda x: len(x))

print(sorted_strings)


# Ans.  10.
def common_element(L1, L2):
    return set(L1) & set(L2)


list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]

print(list(common_element(list1, list2)))

# Ans.  11.
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


print(factorial(5))

# Ans.  12.


def fibonacci(n):
    if n <= 0:
        raise ValueError("Input n must be a positive integer.")
    if n == 1 or n == 2:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


# Test the function
n = 6
print(f"F({n}) =", fibonacci(n))

# Ans.  13.


def fun(List):
    if not List:
        return 0
    else:
        return List[0] + fun(List[1:])


List = [1, 2, 3, 4, 5]

Total_sum = fun(List)
print(f"The sum of all element in the list is {Total_sum}")

# Ans.  14.
def palindrome(s):
    if len(s) <= 1:
        return True

    if s[0] == s[-1]:
        return palindrome(s[1:-1])

    else:
        return False


print(palindrome("radar"))

# Ans.  15.
def gcd_recursive(a, b):
    if b == 0:
        return a
    else:
        return gcd_recursive(b, a % b)


num1 = 24
num2 = 36

result = gcd_recursive(num1, num2)
print(f"The GCD of {num1} and {num2} is: {result}")
