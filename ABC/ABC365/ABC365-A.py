Y = int(input())

if Y % 4 != 0:
    print(365)
    exit()

if Y % 100 != 0:
    print(366)
    exit()

if Y % 400 != 0:
    print(365)
    exit()

print(366)
