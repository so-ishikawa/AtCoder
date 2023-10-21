N = int(input())

if N == 2 or N == 3:
    print("Yes")
    exit()

if N % 2 == 0 and N % 3 == 0 and N % 6 == 0:
    print("Yes")
    exit()

print("No")
exit()
