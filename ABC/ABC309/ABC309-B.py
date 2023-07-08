N = int(input())
upper = None
lower = None
middle =[]
for i in range(N):
    if i == 0:
        upper = input()
        continue
    if i == N-1:
        lower = input()
        continue
    middle.append(input())
if N != 2:
    print(middle[0][0], end="")
    print(upper[:-1])
    for i in range(N-2):
        # print("debug:", i, middle)
        if i ==  N-3:
            print(lower[0], end="")
        else:
            print(middle[i+1][0], end="")
        print(middle[i][1:-1], end="")
        if i == 0:
            print(upper[-1], end="")
        else:
            print(middle[i-1][-1:], end="")
        print("")
    print(lower[1:], end="")
    print(middle[-1][-1])
    exit()
# N == 2
print(lower[0], end="")
print(upper[0])
print(lower[1], end="")
print(upper[-1])
