N = int(input())
A_list = list(map(int, input().split()))

memo = dict()
for index in range(len(A_list)):
    a = A_list[index]
    if a in memo:
        print(memo[a])
        memo[a] = index + 1
        continue
    memo[a] = index + 1
    print(-1)
