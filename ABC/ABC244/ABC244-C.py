N = int(input())
temp = set()
while True:
    for i in range(1, 2*N+1+1):
        if i in temp:
            continue
        print(i)
        temp.add(i)
        break
    aoki_output = int(input())
    if aoki_output == 0:
        exit()
    temp.add(aoki_output)
