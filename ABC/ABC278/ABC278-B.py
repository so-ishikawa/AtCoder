H, M = map(int, input().split())


h = H
m = M

while True:
    A = int(h / 10)
    B = int(h % 10)
    C = int(m / 10)
    D = int(m % 10)
    # print(A,B,C,D)
    if not ( (A == 2 and C > 3) or B > 5 ):
        print(h, m)
        break
 
    m = m + 1
    if m == 60:
        m = 0
        h = h + 1
        if h == 24:
            h = 0
