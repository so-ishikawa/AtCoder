N = int(input())
S_list = []

sum_value = 0
for _ in range(N):
    s, c = map(str, input().split())
    c = int(c)
    sum_value += c
    S_list.append(s)

S_list.sort()

print(S_list[sum_value%N])


