N, D = map(int, input().split())
TL_list = []
for i in range(N):
    T, L = map(int, input().split())
    TL_list.append((T, L))


for d in range(1, D+1):
    max_ = -1
    max_index = -1
    for index in range(len(TL_list)):
        t, l = TL_list[index]
        temp = t * (l+d)
        if temp > max_:
            max_ = temp
            max_index = index
    print(max_)
