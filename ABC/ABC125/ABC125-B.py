N = int(input())
V_list = list(map(int, input().split()))
C_list = list(map(int, input().split()))

temp = [v - c for (v, c) in zip(V_list, C_list)]
print(sum([x for x in temp if x > 0]))
