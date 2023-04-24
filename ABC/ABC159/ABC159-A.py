N, M = map(int, input().split())

result = 0
for i in [N, M]:
    if i == 0 or i == 1:
        continue
    if i == 2:
        result += 1
        continue
    result = result + int(i * (i-1) / 2)

print(result)
