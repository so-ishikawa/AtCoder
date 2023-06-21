import math

a = int(input())
b = int(input())
n = int(input())

temp = int(a * b / math.gcd(a, b))
if n % temp == 0:
    print(n)
    exit()
print(((n//temp)+1)*temp)
