N, M = map(int, input().split())
A_list = list(map(int, input().split()))
B_list = list(map(int, input().split()))

C = A_list + B_list
C.sort()

count = 0
for c in C:
    if count == 0 and c in A_list:
        count = 1
        continue
    if c in A_list:
        print("Yes")
        exit()
    count = 0
print("No")
