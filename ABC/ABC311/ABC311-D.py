import sys
sys.setrecursionlimit(20000000)

N, M = map(int, input().split())
S_list = []
for i in range(N):
    S_list.append(input())

moved_list = []
for i in range(N):
    temp = []
    for j in range(M):
        temp_ = [False, False, False, False]
        temp.append(temp_)
    moved_list.append(temp)

# print(moved_list)

passed_list = []
for i in range(N):
    passed_list.append([False]*M)

def f(current_i, current_j):
    for i in range(len(moved_list[current_i][current_j])):
        if moved_list[current_i][current_j][i]:
            # already moved
            continue
        moved_list[current_i][current_j][i] = True
        if i == 0:#up
            temp = current_i
            for k in range(current_i, -1, -1):
                if S_list[k][current_j] == "#":
                    break
                passed_list[k][current_j] = True
                temp = k
            f(temp, current_j)
            continue
        if i == 1:#down
            temp = current_i
            for k in range(current_i, N):
                if S_list[k][current_j] == "#":
                    break
                passed_list[k][current_j] = True
                temp = k
            f(temp, current_j)
            continue
        if i == 2:#left
            temp = current_j
            for k in range(current_j, -1, -1):
                if S_list[current_i][k] == "#":
                    break
                passed_list[current_i][k] = True
                temp = k
            f(current_i, temp)
            continue
        if i == 3:#right
            temp = current_j
            for k in range(current_j, M):
                if S_list[current_i][k] == "#":
                    break
                passed_list[current_i][k] = True
                temp = k
            f(current_i, temp)
            continue
    

f(2, 2)


print(passed_list)
print(passed_list.count(True))
