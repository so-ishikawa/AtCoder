A, B = map(int, input().split())

if A == B:
    print(1)
    exit()
if not ((A + B)/2).is_integer():
    print(2)
    exit()
print(3)
