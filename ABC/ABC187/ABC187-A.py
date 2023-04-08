A, B = map(int, input().split())

A_ = A // 100 + (A % 100) // 10 + A % 10
B_ = B // 100 + (B % 100) // 10 + B % 10

# print("!", A//100+(A//100))

if A_ == B_:
    print(A_)
    exit()

print(max(A_, B_))
