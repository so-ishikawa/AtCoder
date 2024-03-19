N, M = map(int, input().split())
D_list = list(map(int, input().split()))
D_list.sort()

masu = [False]*(N+1)
masu[0] = True

for current_position in range(N+1):
    if not masu[current_position]:
        continue
    for dice_value in D_list:
        next_position = current_position + dice_value
        if next_position > N:
            break
        masu[next_position] = True

if masu[N]:
    print("Yes")
    exit()
print("No")
