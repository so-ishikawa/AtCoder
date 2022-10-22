A, B = map(int, input().split())
temp = round(B/A, 3)
s = '{:.3f}'.format(temp)
print(s)
