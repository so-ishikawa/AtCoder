A, B = map(int, input().split())
if B % A == 0:
    print(B//A)
    exit()
print((B//A)+1)
exit()
