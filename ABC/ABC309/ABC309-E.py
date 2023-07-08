import sys
sys.setrecursionlimit(10**6)

N, M = map(int, input().split())
p_list = list(map(int, input().split()))
p_list.insert(0, "dummy")
p_list.insert(0, "dummy")

x_list = []
y_list = []
for i in range(M):
    x, y = map(int, input().split())
    x_list.append(x)
    y_list.append(y)

x_list.insert(0, "dummy")
y_list.insert(0, "dummy")

child_list = []
for i in range(N+1):
    child_list.append([])

child_list[0] = "dummy"

for i in range(2, N+1):
    child_list[p_list[i]].append(i)

insurance_list = [False]*N
insurance_list.insert(0, "dummy")

already_insure_list = [0]*N
already_insure_list.insert(0, "dummy")



def f(target, count):
    if already_insure_list[target] >= count:
        return
    already_insure_list[target] = count
    
    insurance_list[target] = True
    if count != 0:
        count -= 1
        for i in child_list[target]:
            f(i, count)

for i in range(1, len(x_list)):
    f(x_list[i], y_list[i])

print(insurance_list.count(True))
