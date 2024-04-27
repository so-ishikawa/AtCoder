from collections import deque

N = int(input())
A_list = list(map(int, input().split()))

queue = deque()
for a in A_list:
    # print(queue)

    # queue.append(2**a)
    queue.append(a)

    while True:
        if len(queue) <= 1:
            break
        if queue[-1] != queue[-2]:
            break
        temp = queue.pop()
        queue.pop()
        # queue.append(2*temp)
        queue.append(temp+1)


print(len(queue))
# print(queue)
