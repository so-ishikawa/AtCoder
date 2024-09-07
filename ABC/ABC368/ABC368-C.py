N = int(input())
H_list = list(map(int, input().split()))

T = 0
for h in H_list:
    #T = T + 1
    # print(h,T)
    chp = h
    if (T+1) % 3 == 1:
        pass
    elif (T+1) % 3 == 2:
        chp -= 1
        T += 1
        if chp <= 0:
            continue
        chp -= 3
        T += 1
        if chp <= 0:
            continue
    else:
        chp -= 3
        T += 1
        if chp <= 0:
             continue

    temp = chp // 5
    T += temp*3
    if chp % 5 == 0:
        continue
    if chp % 5 == 1:
        T += 1
        continue
    if chp % 5 == 2:
        T += 2
        continue
    else:
        T += 3
        continue
print(T)