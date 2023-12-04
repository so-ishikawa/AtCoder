N = int(input())
H_list = list(map(int, input().split()))

count = 0
for i in range(1, N+1):
    if H_list[i-1] == max(H_list[:i]):
        count += 1
print(count)
