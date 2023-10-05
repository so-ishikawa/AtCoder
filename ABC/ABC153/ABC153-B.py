H, N = map(int, input().split())
A_list = list(map(int, input().split()))

if H > sum(A_list):
    print("No")
    exit()
print("Yes")
