s = input().split()
S = s[0]
T = s[1]
A, B = map(int, input().split())
U = input()

if S == U:
    print(A-1, B)
else:
    print(A, B-1)
