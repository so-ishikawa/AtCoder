H, W = map(int, input().split())
S_list = []
for i in range(H):
    S_list.append(input())

word_list = ["s","n","u","k","e"]
direction_list = [(1,0),(1,1),(0,1),(-1,1),(-1,0),(-1,-1),(0,-1),(1,-1)]

for h in range(H):
    for w in range(W):
        for d in direction_list:
            if not (0 <= h + 4*d[0] and h + 4*d[0] < H and 0 <= w + 4*d[1] and w + 4*d[1] < W):
                continue
            for index in range(len(word_list)):
                if S_list[h+index*d[0]][w+index*d[1]] != word_list[index]:
                    break
                if index == len(word_list)-1:
                    # result
                    for _index in range(len(word_list)):
                        print(h+_index*d[0]+1, w+_index*d[1]+1)

