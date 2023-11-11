from collections import deque
S = input()

dq = deque()

for s in S:
    dq.appendleft(s)

    while True:
        if len(dq) < 3:
            break
        if dq[0] == "C" and dq[1] == "B" and dq[2] == "A":
            dq.popleft()
            dq.popleft()
            dq.popleft()
        else:
            break
        
dq.reverse()
print("".join(list(dq)))

