x, k = map(int, input().split())

for i in range(k):
    current_num = int(x % pow(10, i+1) / pow(10, i))
    x = int(x / pow(10, i+1)) * pow(10, i+1) + 0 * pow(10, i) + x % pow(10, i)
    if current_num >= 5:
        ii = i + 1
        while True:
            next_num = int(x % pow(10, ii+1) / pow(10, ii))
            if next_num != 9:
                next_num += 1
                x = int(x / pow(10, ii+1)) * pow(10, ii+1) + next_num * pow(10, ii) + x % pow(10, ii)
                break
            else:
                x = int(x / pow(10, ii+1)) * pow(10, ii+1) + 0 * pow(10, ii) + x % pow(10, ii)
                ii += 1
                continue
print(x)
