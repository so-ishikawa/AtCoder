A, B, C, X, Y = map(int, input().split())
use = min((A/2 + B/2), C)
temp = min(X, Y) * use * 2
num = max(X, Y) - min(X, Y)

value = A if X > Y else B
temp2 = min(value*num, 2*C*num)
print(int(temp+temp2))
