A, B, C = map(int, input().split())

A_count = [A,B,C].count(A)
B_count = [A,B,C].count(B)

if A_count == 3:
    print("No")
    exit()

if A_count == 1 and B_count == 1:
    print("No")
    exit()

print("Yes")
