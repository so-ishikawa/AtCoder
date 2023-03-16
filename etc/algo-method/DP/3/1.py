import sys

N, M = map(int, input().split())
a_list = list(map(int, input().split()))

masu = []
for i in range(N):
    masu.append([False]*(sum(a_list)+1))

counter = 0

def f(current_y, current_x):
    global masu
    global counter

    if masu[current_y][current_x]:
        return

    masu[current_y][current_x] = True

    if current_y == N-1:
        if current_x < M
            counter += 1
        return


    f(current_y + 1, current_x)
    f(current_y + 1, current_x + a_list[current_y])

f(0, 0)

print(counter)

