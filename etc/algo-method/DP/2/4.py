def factorial(x):
    """
    5! = 1*2*3*4*5
    """
    temp = 1
    for i in range(2, x+1):
        temp = temp * i
    return temp


def r_factorial(x, c):
    """
    10, 5 = 10, 9, 8, 7, 6
    """
    temp = 1
    for i in range(x, x-c, -1):
        temp = temp * i
    return temp


def combination(x, c):
    """
    10C5 = 252
    """
    return(int(r_factorial(x,c)/factorial(c)))


N = int(input())

print(combination(2*(N-1), (N-1)))
