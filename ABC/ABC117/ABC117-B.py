N = int(input())
L_list = list(map(int, input().split()))

if max(L_list) < sum(L_list) - max(L_list):
    print("Yes")
    exit()
print("No")
