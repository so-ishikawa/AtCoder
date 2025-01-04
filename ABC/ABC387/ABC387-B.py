X = int(input())
temp = 0
for i in range(1, 9+1):
    for j in range(1, 9+1):
        if i*j == X:
            continue
        temp += i*j
print(temp)
