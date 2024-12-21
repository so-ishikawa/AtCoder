A, B, C = map(int, input().split())

if A == B == C:
    print("Yes")
    exit()

temp = [A, B, C]
temp.sort()

if temp[0] + temp[1] == temp[2]:
    print("Yes")
    exit()

print("No")
