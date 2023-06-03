import sys
sys.setrecursionlimit(10 ** 9)

# l = list(map(int, input().split()))
N, D = map(int, input().split())
XY_list = []
for i in range(N):
    x, y = map(int, input().split())
    XY_list.append((x, y))

virus_list = [False]*(N-1)
virus_list.insert(0, True)


def f(src_index):
    for target_index in range(N):
        if virus_list[target_index]:
            continue
        if ((XY_list[src_index][0] - XY_list[target_index][0])**2 +  (XY_list[src_index][1] - XY_list[target_index][1])**2)**(1/2) <= D:
            virus_list[target_index] = True
            f(target_index)
        

f(0)




"""
for _ in range(2000):
    for src_index in range(len(XY_list)):
        if not virus_list[src_index]:
            continue
        for target_index in range(len(XY_list)):
            if virus_list[target_index]:
                continue
            if ((XY_list[src_index][0] - XY_list[target_index][0])**2 +  (XY_list[src_index][1] - XY_list[target_index][1])**2)**(1/2) <= D:
                virus_list[target_index] = True
"""
for i in virus_list:
    if i:
        print("Yes")
    else:
        print("No")
