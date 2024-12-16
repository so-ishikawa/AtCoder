N, K = map(int, input().split())
R_list = list(map(int, input().split()))

def f(index, result):
    if index == N:
        temp = [int(x) for x in list(result)]
        if sum(temp) % K != 0:
            return
        for i in temp:
            print(i, end=" ")
        print("")
        return

    for i in range(1, R_list[index]+1):
        f(index+1, result+str(i))

f(0, "")
