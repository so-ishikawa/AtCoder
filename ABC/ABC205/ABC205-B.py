N = int(input())
temp = set(map(int, input().split()))

if N == len(temp):
    print("Yes")
    exit()

print("No")
