N, M = map(int, input().split())
temp = set()

for i in range(M):
    A, B = map(str, input().split())
    A = int(A)
    if B == "F":
        print("No")
        continue
    if A not in temp:
        print("Yes")
        temp.add(A)
        continue
    else:
        print("No")
