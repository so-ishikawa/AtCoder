X, A, B = map(int, input().split())

if A >= B:
    print("delicious")
    exit()
if B - A <= X:
    print("safe")
    exit()
print("dangerous")
exit()
