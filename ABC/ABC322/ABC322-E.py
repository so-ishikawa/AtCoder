N, K, P = map(int, input().split())
C_list = []
A_list = []
emp = [0]*K
for i in range(N):
    temp = list(map(int, input().split()))
    C_list.append(temp[0])
    A_list.append(temp[1:])

for i in A_list:
    emp = [x + y for (x, y) in zip(emp, i)]

if [x for x in emp if x < P] != []:
    print(-1)
    exit()

min_cost = 99999999999999999

def f(_index, _emp, cost):
    # print(_index)
    global min_cost
    if _index == N:
        if min_cost > cost:
            min_cost = cost
        return
    temp = [x - y for (x, y ) in zip(_emp, A_list[_index])]

    if [x for x in temp if x < P] == []:
        f(_index +1, temp, cost - C_list[_index])
    f(_index+1, _emp, cost)

# index = 0
f(0, emp.copy(), sum(C_list))

print(min_cost)
