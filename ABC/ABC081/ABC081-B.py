N = int(input())
A_list = list(map(int, input().split()))

for i in range(1, 100):
    temp = [x for x in A_list if x % (2**i) == 0]
    if len(temp) != N:
        print(i-1)
        exit()
