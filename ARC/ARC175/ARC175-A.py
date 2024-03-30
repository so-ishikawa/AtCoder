N, A, B = map(int, input().split())
S = input()

masu = []
for i in range(2*N+1):
    masu.append([None]*(2*N+1))

masu[0][0] = (0, 0, 0) #(change_count, [(]count, [)]count )

for h in range(2*N):
    for w in range(2*N+1):
        if w > N:
            continue
        if (2*N)-h < w:
            break
        if masu[h][w] is None:
            continue
        # ( is +1   ) is -1
        target_char = S[(h+1)-1]
        if w == 0:
            if target_char == "(":
                # if w+1 <= 2*N:
                if masu[h+1][w+1] is None or masu[h+1][w+1][0] > masu[h][w][0]:
                    masu[h+1][w+1] = (masu[h][w][0], masu[h][w][1], masu[h][w][2])
                continue
            else:
                if masu[h+1][w+1] is None or masu[h+1][w+1][0] > masu[h][w][0]+1:
                    masu[h+1][w+1] = (masu[h][w][0]+1, masu[h][w][1], masu[h][w][2]+1)
                continue
        if target_char == "(":
            if w+1 <= 2*N:
                if masu[h+1][w+1] is None or masu[h+1][w+1][0] > masu[h][w][0]:
                    masu[h+1][w+1] = (masu[h][w][0], masu[h][w][1], masu[h][w][2])
            if w-1 >= 0:
                if masu[h+1][w-1] is None or masu[h+1][w-1][0] > masu[h][w][0]:
                    masu[h+1][w-1] = (masu[h][w][0]+1, masu[h][w][1]+1, masu[h][w][2])
            continue
        else: # ) case
            if w+1 <= 2*N:
                if masu[h+1][w+1] is None or masu[h+1][w+1][0] > masu[h][w][0]:
                    masu[h+1][w+1] = (masu[h][w][0]+1, masu[h][w][1], masu[h][w][2]+1)
            if w-1 >= 0:
                if masu[h+1][w-1] is None or masu[h+1][w-1][0] > masu[h][w][0]:
                    masu[h+1][w-1] = (masu[h][w][0], masu[h][w][1], masu[h][w][2])
            continue

X, Y, Z  = masu[2*N][0]

#stage 2

left = X*B
temp = min(Y, Z)
temp_ = X - 2*temp
right = temp_*B + temp*A
print(min(left, right))
