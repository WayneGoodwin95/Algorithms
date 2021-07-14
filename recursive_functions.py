"""
RECURSION:
    To solve a problem, solve a sub-problem that is a smaller instance of the same problem,
    and then use the solution to that smaller instance to solve the original problem.

    In order for a recursive algorithm to work, the smaller subproblems must eventually arrive at the base case.
    When computing n! the sub-problems get smaller and smaller until we compute 0!
    You must make sure that eventually, you hit the base case.

    Each recursive call should be on a smaller instance of the same problem, that is, a smaller subproblem.
    The recursive calls must eventually reach a base case, which is solved without further recursion.
"""


# factorial of an integer
def fac_func(n):
    result = n
    for i in range((n - 1), 1, -1):
        result *= i
    return str(result)


print("The value of 5! should be " + str(5 * 4 * 3 * 2 * 1))
print("The value of 5! is " + fac_func(5))
print("The value of 0! should be 1")
print("The value of 0! is " + fac_func(0) + "\n")


# RECURSIVE factorial of an integer
def fac_func(n):
    if n == 0:
        n = 1
        return 1
    else: return fac_func(n - 1) * n


print("The value of 5! should be " + str(5 * 4 * 3 * 2 * 1))
print("The value of 5! is " + str(fac_func(5)))
print("The value of 5! should be " + str(4 * 3 * 2 * 1))
print("The value of 5! is " + str(fac_func(4)))
print("The value of 5! should be " + str(3 * 2 * 1))
print("The value of 5! is " + str(fac_func(3)))
print("The value of 0! should be 1")
print("The value of 0! is " + str(fac_func(0)) + '\n')


# RECURSIVE is a string a palindrome
def palindrome(s):
    if len(s) == 1:
        return True
    elif len(s) == 2:
        if s[0] == s[1]:
            return True
        else: return False
    else:
        if s[0] == s[-1]:
            return palindrome(s[1:-1])
        else:
            return False

print(palindrome('SS'))
print(palindrome('DS'))
print(palindrome('S'))
print("is MOTOR a palindrome? " + str(palindrome('MOTOR')))
print("is MADAM a palindrome? " + str(palindrome('MADAM')) + "\n")


# Recursive Powers
def rec_pow(x, n):
    if n == 0: # Base-case
        return 1
    elif n < 0: # Negative
        return 1 / (rec_pow(x, -n))
    elif n > 0 and n % 2 == 1: # Odd (positive)
        return x * (rec_pow(x, n-1))
    elif n > 0 and n % 2 == 0: # Even (positive)
        y = rec_pow(x, n/2)
        return y*y


print('power(x = 3, n = 0) ' + str(rec_pow(3, 0)) + ' 1')
print('power(x = 3, n = 1) ' + str(rec_pow(3, 1)) + ' 3')
print('power(x = 3, n = 2) ' + str(rec_pow(3, 2)) + ' 9')
print('power(x = 3, n = 2) ' + str(rec_pow(3, 3)) + ' 27')
print('power(x = 3, n = -1) ' + str(rec_pow(3, -1)) + ' 1/3')
print('power(x = 3, n = -1) ' + str(rec_pow(3, -3)) + ' 1/27')