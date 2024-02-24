N = int(input())
P_list = list(map(int, input().split()))

Q = int(input())
AB_list = []
for _ in range(Q):
    a, b = map(int, input().split())
    AB_list.append((a, b))

dic = dict()
for i in range(1, N+1):
    dic[P_list[i-1]] = i

for i in AB_list:
    print(i[0] if dic[i[0]] < dic[i[1]] else i[1])
