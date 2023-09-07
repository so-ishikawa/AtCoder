from collections import defaultdict

N = int(input())
A_list = list(map(int, input().split()))
Q = int(input())
bc_list = []
for i in range(Q):
    b, c = map(int, input().split())
    bc_list.append((b, c))

dic = defaultdict(lambda: 0)
for i in A_list:
    dic[i] = dic[i] + 1
sum_value = sum(A_list)

result = [0]*Q
count = 0
for bc in bc_list:
    b = bc[0]
    c = bc[1]
    num = dic[b]
    _b = b*num
    _c = c*num
    diff = _c - _b
    sum_value += diff
    dic[c] = dic[c] + num
    dic[b] = 0
    result[count] = sum_value
    count += 1

print(*result, sep="\n")
