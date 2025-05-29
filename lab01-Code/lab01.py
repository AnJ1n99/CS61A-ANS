def both_odd(a, b):
    """Returns True if both a and b are odd numbers.

    >>> both_odd(-1, 1)
    True
    >>> both_odd(2, 1)
    False
    """
    return a % 2 == 1 and b % 2 == 1


def factorial(n):
    """Return the factorial of a positive integer n.

    >>> factorial(3)
    6
    >>> factorial(5)
    120
    """
    ans = 1   
    while n > 1:   #base case : when n < 0,quit this iteration 1 
        ans = ans * n 
        n = n - 1   
    return ans  # YOUR CODE HERE






def is_triangle(a, b, c):
    """Given three integers (may be nonpositive), judge whether the three
    integers can form the three sides of a triangle.

    >>> is_triangle(2, 1, 3)
    False
    >>> is_triangle(5, -3, 4)
    False
    >>> is_triangle(2, 2, 2)
    True
    """
    return  a + b > c and a + c > b and b + c > a# YOUR CODE HERE


def number_of_six(n):
    """Return the number of 6 in each digit of a positive integer n.

    >>> number_of_six(666)
    3
    >>> number_of_six(123456)
    1
    """
    ans = 0
    while n > 0:
        if n % 10 == 6:
            ans = ans + 1
        n = n // 10
    return ans


def max_digit(x):
    """Return the max digit of x.

    >>> max_digit(10)
    1
    >>> max_digit(4224)
    4
    >>> max_digit(1234567890)
    9
    >>> # make sure that you are using return rather than print
    >>> a = max_digit(123)
    >>> a
    3
    """
    maxAns = 0
    while x > 0:
        if x % 10 > maxAns:
            maxAns = x % 10
        x = x // 10
    return maxAns
