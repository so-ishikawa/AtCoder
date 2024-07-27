N, T, P = map(int, input().split())
L_list = list(map(int, input().split()))

if len([x for x in L_list if x >= T]) >= P:
    print(0)
    exit()

L_list.sort(reverse=True)

print(T-L_list[P-1])
