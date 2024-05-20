N = int(input())
H_list = list(map(int, input().split()))

if H_list[0] == max(H_list):
    print(-1)
    exit()

for i in range(1, N+1):
    if H_list[0] < H_list[i]:
        print(i+1)
        exit()


