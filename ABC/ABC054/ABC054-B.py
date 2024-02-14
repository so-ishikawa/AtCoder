N, M = map(int, input().split())
A_list = []
B_list = []

for _ in range(N):
    A_list.append(input())

for _ in range(M):
    B_list.append(input())

if N == M:
    flag = True
    for m_h in range(M):
        for m_w in range(M):
            _h = m_h
            _w = m_w
            if A_list[_h][_w] != B_list[m_h][m_w]:
                # print(_h, _w, m_h, m_w)
                flag = False
                break
        if not flag:
            break
    if flag:
        print("Yes")
        exit()
    print("No")

for h_diff in range(N-M):
    for w_diff in range(N-M):
        flag = True
        for m_h in range(M):
            for m_w in range(M):
                _h = m_h + h_diff
                _w = m_w + w_diff
                if A_list[_h][_w] != B_list[m_h][m_w]:
                    # print(_h, _w, m_h, m_w)
                    flag = False
                    break
            if not flag:
                break
        if flag:
            print("Yes")
            exit()
print("No")
