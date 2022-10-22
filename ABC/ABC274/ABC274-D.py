N, x, y = map(int, input().split())
A_list = list(map(int, input().split()))

start_point = [0, 0]
for i in range(N):
    if i % 4 == 0:
        start_point[0] += A_list[i]
    elif i % 4 == 1:
        start_point[1] += A_list[i]
    elif i % 4 == 2:
        start_point[0] -= A_list[i]
    else:
        start_point[1] -= A_list[i]

if start_point[0] == x and start_point[1] == y:
    print("Yes")
else:
    print("No")
