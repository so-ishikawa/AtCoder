N = int(input())
A_list = []
for i in range(N):
    A_list.append(input())

direction = [(1,1),(1,0),(1,-1),(0,1),(0,-1),(-1,1),(-1,0),(-1,-1)]

max_value = 0
for i in range(N):
    for j in range(N):
        for k in direction:
            temp = 0
            for l in range(N):
                temp = temp + int(A_list[(i+k[0]*l)%(N)][(j+k[1]*l)%(N)]) * (10**(N-1-l))
            if max_value < temp:
                max_value = temp

print(max_value)
