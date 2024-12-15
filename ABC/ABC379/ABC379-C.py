N, M = map(int, input().split())
X_list = list(map(int, input().split()))
A_list = list(map(int, input().split()))

pairs = []
for i in range(len(X_list)):
    pairs.append((X_list[i], A_list[i]))
pairs.sort(key=lambda x: x[0])

X_list.clear()
A_list.clear()

for i in range(len(pairs)):
    X_list.append(pairs[i][0])
    A_list.append(pairs[i][1])


stone_position = [x-1 for x in X_list]

if sum(A_list) != N:
    print(-1)
    exit()

if stone_position[0] != 0:
    print(-1)
    exit()

stone_start_position = [stone_position[0]]
temp = stone_position[0]
for i in range(len(A_list)-1):
    temp += A_list[i]
    stone_start_position.append(temp)

for i in range(len(stone_position)):
    if stone_position[i] > stone_start_position[i]:
        print(-1)
        exit()
result = 0
for i in range(len(stone_position)):
    diff = stone_start_position[i] - stone_position[i]
    n = A_list[i]
    result += (((n-1)*n)//2 + diff*n)

print(result)
