A, B, C, D = map(int, input().split())

Alice = set(range(A, B+1))
Bob = set(range(C, D+1))

temp = Alice & Bob
if len(temp) == 0:
    print(0)
    exit()
print(max(temp) - min(temp))
