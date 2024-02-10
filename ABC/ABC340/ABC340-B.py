Q = int(input())
temp = []
for _ in range(Q):
    num, xk = map(int, input().split())
    if num == 1:
        temp.append(xk)
        continue
    if num == 2:
        print(temp[-1*xk])
