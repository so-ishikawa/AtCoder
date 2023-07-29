N, M = map(int, input().split())
S_list = []
for i in range(N):
    S_list.append(input())

def f(n, m):
    black = [(n,m),(n,m+1),(n,m+2),(n+1,m),(n+1,m+1),(n+1,m+2),(n+2,m),(n+2,m+1),(n+2,m+2),
             (n+6,m+6),(n+6,m+7),(n+6,m+8),(n+7,m+6),(n+7,m+7),(n+7,m+8),(n+8,m+6),(n+8,m+7),(n+8,m+8)]
    white = [(n, m+3),(n+1,m+3),(n+2,m+3),(n+3,m),(n+3,m+1),(n+3,m+2),(n+3,m+3),
             (n+5,m+5),(n+5,m+6),(n+5,m+7),(n+5,m+8),(n+6,m+5),(n+7,m+5),(n+8,m+5)]
    return(black, white)

result = []
for n in range(N):
    for m in range(M):
        # print(n, m, "!", result)
        # n = 0
        # m = 9
        if n + 9 > N or m + 9 > M:
            continue
        black, white = f(n, m)
        #print(black, white)
        false_flag = False
        for i in black:
            if S_list[i[0]][i[1]] != "#":
                false_flag = True
                # print("A")
                break
        if false_flag:
            # print("B")
            continue

        for i in white:
            if S_list[i[0]][i[1]] != ".":
                false_flag = True
                # print("C")
                break
        if false_flag:
            # print("D")
            continue
        # print("E")
        result.append((n, m))
        # print(result)
        # exit()
# print(result)
result.sort(key=lambda x: (x[0], x[1]))
for i in result:
    print(i[0]+1,i[1]+1)
