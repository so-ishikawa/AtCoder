a = int(input())
b = int(input())

if a % b == 0:
    print(0)
    exit()

print(b - (a % b))
exit()
