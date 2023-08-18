N = int(input())
A_list = list(map(int, input().split()))
B_list = list(map(int, input().split()))

temp = 0
for i in range(N):
    temp = temp + A_list[i] * B_list[i]

if temp == 0:
    print("Yes")
    exit()

print("No")
