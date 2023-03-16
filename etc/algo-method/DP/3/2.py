import sys

N, M = map(int, input().split())
w_list = list(map(int, input().split()))

def f(index, sum_weight):
    global M
    if index > N-1:
        return
    update_weight = sum_weight + w_list[index]
    if update_weight == M:
        print("Yes")
        sys.exit(0)
    if update_weight > M:
        return

    f(index+1, sum_weight)
    f(index+1, update_weight)

f(0, 0)
print("No")
