H, W = map(int, input().split())
S_list = []
for i in range(H):
    S_list.append(input())

Sensor_list = []
for i in range(H):
    Sensor_list.append([False]*W)

dir_list = [(1,1),(1,0),(1,-1),(0,1),(0,-1),(-1,1),(-1,0),(-1,-1)]

for h in range(H):
    for w in range(W):
        if S_list[h][w] != "#":
            continue
        find_flag = False
        for d in dir_list:
            dy, dx = d
            ny = h + dy
            nx = w + dx
            if ny < 0 or nx < 0 or ny >= H or nx >= W:
                continue
            if S_list[ny][nx] != "#":
                continue
            find_flag = True
            
            #src = (h, w)
            # dst = (ny, nx)

            src = None
            if Sensor_list[h][w] == True or Sensor_list[h][w] == False:
                src = (h, w)
            else:
                _h = h
                _w = w
                while Sensor_list[_h][_w] != True:
                    _h, _w = Sensor_list[_h][_w]
                src = (_h, _w)

            dst = None
            if Sensor_list[ny][nx] == True or Sensor_list[ny][nx] == False:
                dst = (ny, nx)
            else:
                _h = ny
                _w = nx
                while Sensor_list[_h][_w] != True:
                    _h, _w = Sensor_list[_h][_w]
                dst = (_h, _w)

            if src < dst:
                Sensor_list[h][w] = src
                Sensor_list[ny][nx] = src
                Sensor_list[dst[0]][dst[1]] = src
                Sensor_list[src[0]][src[1]] = True
            else:
                Sensor_list[h][w] = dst
                Sensor_list[ny][nx] = dst
                Sensor_list[src[0]][src[1]] = dst
                Sensor_list[dst[0]][dst[1]] = True
    

        if not find_flag:
            Sensor_list[h][w] = True
            continue

count = 0
for i in Sensor_list:
    count += i.count(True)
print(count)
