H, W, N = map(int, input().split())


#(y, x)
white_direction_dic = {(-1, 0):(0, 1), (0,1):(1, 0), (1,0):(0, -1), (0,-1):(-1,0)}
black_direction_dic = {(-1, 0):(0, -1), (0, -1):(1,0), (1,0):(0, 1), (0,1):(-1,0)}

# N = 5

ban = []
for _ in range(H):
    ban.append(["."]*W)

current_position = (0, 0)
current_direction = (-1, 0)

for n in range(N):
    if ban[current_position[0]][current_position[1]] == ".":
        ban[current_position[0]][current_position[1]] = "#"
        next_direction = white_direction_dic[(current_direction)]
        # print(next_direction, "!!")
        current_position = ((current_position[0]+next_direction[0])%H, (current_position[1]+next_direction[1])%W)
        # print(current_position, "!")
        """
        if ban[current_position[0]][current_position[1]] == ".":
            ban[current_position[0]][current_position[1]] = "#"
        else:
            ban[current_position[0]][current_position[1]] = "."
        """ 
    else:
        ban[current_position[0]][current_position[1]] = "."
        next_direction = black_direction_dic[(current_direction)]
        current_position = ((current_position[0]+next_direction[0])%H, (current_position[1]+next_direction[1])%W)
        """
        if ban[current_position[0]][current_position[1]] == ".":
            ban[current_position[0]][current_position[1]] = "#"
        else:
            ban[current_position[0]][current_position[1]] = "."
        """
    current_direction = next_direction

for h in range(H):
    for w in range(W):
        print(ban[h][w], end="")
    print("")


