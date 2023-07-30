N = int(input())
A_list = list(map(int, input().split()))

temp = 0
for i in A_list:
    if i <= 10:
        continue
    temp = temp + i - 10
print(temp)
