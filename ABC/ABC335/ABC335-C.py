from collections import deque
"""
que = deque()
que.appendleft("1")
que.appendleft("2")
que.pop()
print(que[0])
"""
que = deque()
N, Q = map(int, input().split())

for i in range(1, N+1):
    que.append((i, 0))


for i in range(1, Q+1):
    num, char = map(str, input().split())
    if num == "1":
        x, y = que[0]
        if char == "R":
            new_posi = (x+1, y)#(que[0][0]+1, que[0][1])
            que.appendleft(new_posi)
            que.pop()
        elif char == "L":
            new_posi = (x-1, y)#(que[0][0]-1, que[0][1])
            que.appendleft(new_posi)
            que.pop()
        elif char == "U":
            new_posi = (x, y+1)#(que[0][0], que[0][1]+1)
            que.appendleft(new_posi)
            que.pop()
        else: #D
            new_posi = (x, y-1)#(que[0][0], que[0][1]-1)
            que.appendleft(new_posi)
            que.pop()
    else:
        # "2"case
        print(que[int(char)-1][0], que[int(char)-1][1])
        # print(que)
