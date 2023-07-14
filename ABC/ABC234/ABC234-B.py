N = int(input())
xy_list = []
for i in range(N):
    x, y = map(int, input().split())
    xy_list.append((x,y))

max_length = 0
for i in range(len(xy_list)):
    for j in range(i+1,len(xy_list)):
        temp = (xy_list[i][0] - xy_list[j][0])**2 + (xy_list[i][1] - xy_list[j][1])**2
        if max_length < temp:
            max_length = temp
print((max_length)**(1/2))

