N, M = map(int, input().split())








result = []

start_max = M-10*(N-1)


def f(_result, _count, _min):
    global result
    global N
    global M
    global start_max
    _max = start_max + _count*10
    if _count == N:
        result.append(_result)
        return
    for i in range(_min, _max+1):
        if i+10 > _max:
            break

        temp = _result.copy()
        temp.append(i+10)

        f(temp, _count+1, i+10)


for i in range(1, (M-10*(N-1))+1):
    f([i], 1, i)

print(len(result))
for i in result:
    for j in i:
        print(j, end=" ")
    print("")

