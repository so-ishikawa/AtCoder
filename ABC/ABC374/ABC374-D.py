import itertools

N, S, T = map(int, input().split())
ABCD_list = []
for _ in range(N):
    a, b, c, d = map(int, input().split())
    ABCD_list.append((a,b,c,d))

min_time = 99999999999999999999999999999

def f(permu, index, last_points, sum_time):
    # print(permu, index, last_points, sum_time)
    global min_time
    if index == N:
        if sum_time < min_time:
            min_time = sum_time
        return
    
    current_index = permu[index]
    points = ABCD_list[current_index]

    cut_time = ((points[0]-points[2])**2 + (points[1]-points[3])**2)**(1/2)/T
    #X start a, b
    move_time = ((points[0] - last_points[0])**2 + (points[1] - last_points[1])**2)**(1/2)/S
    f(permu, index+1, (points[2], points[3]), sum_time + move_time + cut_time)
    
    #Y start c, d
    move_time = ((points[2] - last_points[0])**2 + (points[3] - last_points[1])**2)**(1/2)/S
    f(permu, index+1, (points[0], points[1]), sum_time + move_time + cut_time)
    

    return


for permu in itertools.permutations(range(N), N):
    f(permu, 0, (0,0), 0)


print(min_time)
