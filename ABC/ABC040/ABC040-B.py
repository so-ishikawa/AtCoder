n = int(input())
min_value = 999999999999999999999
for h in range(1, int(n**(1/2))):
    for w in range(1, n-h):
        temp = abs(h-w) + n - (h*w)
        if min_value > temp:
            min_value = temp
print(min_value)
