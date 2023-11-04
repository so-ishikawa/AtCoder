N = int(input())
A_list = list(map(int, input().split()))

temp = 0
for i in A_list:
    temp = temp + (1/i)

if temp == 0:
    print(0)
    exit()

print(1/temp)
