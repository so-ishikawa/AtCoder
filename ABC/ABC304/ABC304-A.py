# l = list(map(int, input().split()))
N = int(input())
S_list = []
A_list = []
for i in range(N):
    s, a = map(str, input().split())
    a = int(a)
    S_list.append(s)
    A_list.append(a)

min_A_index = A_list.index(min(A_list))
for i in range(min_A_index, len(S_list)):
    print(S_list[i])

for i in range(0, min_A_index):
    print(S_list[i])
