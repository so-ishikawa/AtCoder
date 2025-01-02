N, M = map(int, input().split())
S_list = list(map(str, input().split()))
T_set = set(map(str, input().split()))

for s in S_list:
    if s in T_set:
        print("Yes")
        continue
    print("No")
