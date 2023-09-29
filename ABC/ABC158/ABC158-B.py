N, A, B = map(int, input().split())

rest = N % (A+B)
count = N // (A+B)

if rest < A:
    print(count*A + rest)
    exit()
print(count*A + A)
exit()
