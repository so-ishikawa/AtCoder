N = int(input())
dish_list = []
for i in range(N):
    state, value = map(int, input().split())
    dish_list.append((state, value))
dish_list.insert(0, None) #dummy

temp = []
for i in range(N+1):
    temp.append([None, None])

temp[0][0] = 0
temp[0][1] = 0

for i in range(1, N+1):
    if dish_list[i][0] == 1: #poison
        temp[i][0] = temp[i-1][0] #pass case
        temp[i][1] = max(temp[i-1][0] + dish_list[i][1], temp[i-1][1]) # eat poison with normal or pass poison with bad state
        continue
    # cure drag
    temp[i][0] = max(temp[i-1][0], temp[i-1][0]+dish_list[i][1], temp[i-1][1]+dish_list[i][1]) # pass(normal), eat(normal), eat(poison)
    temp[i][1] = temp[i-1][1] # pass case
print(temp)   
print(max(temp[N][0], temp[N][1]))
