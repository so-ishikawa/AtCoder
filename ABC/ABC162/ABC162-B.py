N = int(input())

sum_value = 0
for i in range(1, N+1):
    if i % 15 == 0:
        continue
    if i % 3 == 0:
        continue
    if i % 5 == 0:
        continue
    sum_value += i
print(sum_value)
