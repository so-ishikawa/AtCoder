n = int(input())
# n = 999999
temp_1 = 1
temp_2 = 0
temp_3 = 0
current = -1

if n == 1:
    print(0)
    exit()
if n == 2:
    print(0)
    exit()
if n == 3:
    print(1)
    exit()

for i in range(4, n+1):
    current = (temp_1 + temp_2 + temp_3) % 10007
    if i == n:
        print(current % 10007)
    temp_3 = temp_2
    temp_2 = temp_1
    temp_1 = current
