# from collections import deque

que_list = []#deque([])
N, Q = map(int, input().split())
# for i in range(1, N+1):
#     que_list.insert(0, (i, 0))

que_list = [(i, 0) for i in range(N, 0, -1)]

for _ in range(Q):
    num, op = map(str, input().split())
    if num == "1":
        # x, y = que_list[-1]
        if op == "R":
            que_list.append((que_list[-1][0]+1, que_list[-1][1]))
        elif op == "L":
            que_list.append((que_list[-1][0]-1, que_list[-1][1]))
        elif op == "U":
            que_list.append((que_list[-1][0], que_list[-1][1]+1))
        else: # "D"
            que_list.append((que_list[-1][0], que_list[-1][1]-1))
        continue            
    else:
        # num == "2"
        op = int(op)
        print(que_list[-1*op][0], que_list[-1*op][1])
