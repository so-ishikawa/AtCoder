N = int(input())
temp = list(str(N))
result = sum([int(x) for x in temp])
if N % result == 0:
    print("Yes")
    exit()
print("No")
