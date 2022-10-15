s = int(input())

if s == 0:
    print(1)
else:
    k = 1
    for i in range(s, 1, -1):
        k = k * i
    print(k)
