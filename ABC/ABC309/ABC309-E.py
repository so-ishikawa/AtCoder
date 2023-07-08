import sys
sys.setrecursionlimit(10**6)

N, M = map(int, input().split())
p_list = list(map(int, input().split()))
p_list.insert(0, "dummy")
p_list.insert(0, "dummy")


x_y_list = []
for i in range(M):
    x, y = map(int, input().split())
    x_y_list.append((x, y))

x_y_list.sort(key=lambda x: (x[1], x[0]), reverse=True)

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
    if already_insure_list[target] > count:
        return
    already_insure_list[target] = count
    
    insurance_list[target] = True
    if count != 0:
        count -= 1
        for i in child_list[target]:
            f(i, count)

for i in range(len(x_y_list)):
    f(x_y_list[i][0], x_y_list[i][1])

print(insurance_list.count(True))
