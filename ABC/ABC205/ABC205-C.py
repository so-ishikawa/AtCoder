import math
A, B, C = map(int, input().split())

def _pow(x, y):
    if y == 1:
        return(x)
    return(x*x)

if C % 2 == 0:
    C = 2
else:
    C = 1
if A == B:
    print("=")
    exit()
if abs(A) == abs(B) and C == 2:
    print("=")
    exit()

    
if _pow(A, C) > _pow(B, C):
    print(">")
else:
    print("<")
