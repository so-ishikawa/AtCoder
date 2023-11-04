M_list = []
for _ in range(9):
    m = list(map(int, input().split()))
    M_list.append(m)

for gyo in M_list:
    for i in range(1, 9+1):
        if i not in gyo:
            print("No")
            exit()

retu = []
for w in range(1, 9+1):
    retu = []
    for h in range(1, 9+1):
        retu.append(M_list[h-1][w-1])
    for i in range(1, 9+1):
        if i not in retu:
            print("No")
            exit()

masu = []
for w in range(0, 9, 3):
    for h in range(0, 9, 3):
        masu = []
        for _w in range(3):
            for _h in range(3):
                masu.append(M_list[h+_h][w+_w])
        for i in range(1, 9+1):
            if i not in masu:
                print("No")
                exit()
print("Yes")
                
