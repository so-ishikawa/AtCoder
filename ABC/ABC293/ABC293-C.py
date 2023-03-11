"""
#str型で受け取るとき
s = input()
#int型で受け取るとき
s = int(input())

A, B = map(int, input().split())

#list型で取得
l = list(map(int, input().split()))
"""
import copy

H, W = map(int, input().split())
A_list = []
for i in range(H):
    temp = list(map(int, input().split()))
    A_list.append(temp)

counter = 0

def f(h, w, _set):
    global counter

    if A_list[h][w] in _set:
        return
    
    if (h == H - 1) and (w == W - 1):
        # print(_set)
        counter += 1
        return

    _set.add(A_list[h][w])

    if h < H - 1:
        f(h+1, w, copy.copy(_set))
    if w < W - 1:
        f(h, w+1, copy.copy(_set))


f(0, 0, set({}))
print(counter)
