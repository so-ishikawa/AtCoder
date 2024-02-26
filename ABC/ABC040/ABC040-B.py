n = int(input())
min_value = 9999999999999999999999
for h in range(1, n+1):
    w = n // h
    temp = n % (h*w)
    if min_value > temp + abs(h-w):
        min_value = temp + abs(h-w)
print(min_value)
