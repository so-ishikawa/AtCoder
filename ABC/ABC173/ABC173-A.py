N = int(input())
b = N // 1000
if N % 1000 == 0:
    print(0)
    exit()
print((b+1)*1000-N)
