N, K = map(int, input().split())
AB_list = []

for i in range(N):
    A, B = map(int, input().split())
    AB_list.append((A, B))

AB_list.sort(key=lambda x: x[0])

money = K
current = 0
for AB in AB_list:
    A, B = AB
    if A - current > money:
        print(current+money)
        exit()
    money = money - (A - current)
    money += B
    current = A

print(current+money)
