H = int(input())

count = 0
total = 0
while True:
    if H < total + 2**count:
        count += 1
        break
    total = total + 2**count
    count += 1
    # print(total)

print(count)
