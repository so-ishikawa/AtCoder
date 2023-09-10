X = int(input())
temp = 100
count = 0
while temp < X:
    count += 1
    temp += temp//100 #int(temp * 1.01)

print(count)
