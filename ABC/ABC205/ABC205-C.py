import math
A, B, C = map(int, input().split())

if C > 0:
    if A > B:
        print(">")
        exit()
    if A == B:
        print("=")
        exit()
    if A < B:
        print("<")
        exit()
if C == 0:
    print("=")
    exit()

if C < 0:
    if A > B:
        print("<")
        exit()
    if A == B:
        print("=")
        exit()
    if A < B:
        print(">")
        exit()


