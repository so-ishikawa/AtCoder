N = int(input())
A_list = list(map(int, input().split()))

count = 0
for i in range(len(A_list)-2):
    if A_list[i] == A_list[i+2]:
        count += 1
print(count)
