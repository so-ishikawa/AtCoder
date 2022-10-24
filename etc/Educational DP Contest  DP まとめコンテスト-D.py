N, W = map(int, input().split())
wv_list = []
for _ in range(N):
    w, v = map(int, input().split())
    wv_list.append((w, v))

dp_list = []
for _ in range(N+1):
    dp_list.append([0]*(W+1))
"""
for i in range(1, N+1):
    for w in range(W+1):
        if wv_list[i-1][0] > w:
            dp_list[i][w] = dp_list[i-1][w]
        else:
            dp_list[i][w] = max(dp_list[i-1][w], wv_list[i-1][1] + dp_list[i-1][w - wv_list[i-1][0]])
print(dp_list[N][W])
"""


"""
def f(i, w):
    if i == 0:
        return 0
    if wv_list[i-1][0] > w:
        return f(i-1, w)
    return max(f(i-1, w), wv_list[i-1][1] + f(i-1, w-wv_list[i-1][0]))

print(f(N, W))
"""

dp_list2 = [0] * (W+1)
for i in range(1, N+1):
    for w in range(W, 0-1, -1):
        if wv_list[i-1][0] <=  w:
            dp_list2[w] = max(dp_list2[w], wv_list[i-1][1]+dp_list2[w-wv_list[i-1][0]])
print(dp_list2[len(dp_list2)-1])















