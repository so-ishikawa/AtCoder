N = int(input())

if N == 0:
    print("#")
    exit()

carpet = []
for i in range(3**N):
    carpet.append(["."]*(3**N))

def f(h, w, level):
    # print(h,w)
    if level == 1:
        carpet[h][w] = "#"
        carpet[h][w+1] = "#"
        carpet[h][w+2] = "#"
        carpet[h+1][w] = "#"
        carpet[h+1][w+2] = "#"
        carpet[h+2][w] = "#"
        carpet[h+2][w+1] = "#"
        carpet[h+2][w+2] = "#"
        return

    for _h in range(3):
        for _w in range(3):
            if _h == 1 and _w == 1:
                continue
            f(((3**level)//3)*_h+h, ((3**level)//3)*_w+w, level-1) 

f(0, 0, N)

for i in range(3**N):
    print(*carpet[i], sep="")

