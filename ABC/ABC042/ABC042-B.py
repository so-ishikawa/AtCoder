N, L = map(int, input().split())
S_list = []
for _ in range(N):
    S_list.append(input())

S_list.sort()
print("".join(S_list))
