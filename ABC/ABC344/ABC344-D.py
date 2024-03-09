T = input()
N = int(input())
temp = []
dic = dict()

for _ in range(N):
    temp_ = list(map(str, input().split()))
    temp_.pop(0)
    temp = temp + temp_

for i in temp:
    if i[0] in dic:
        dic[i[0]].append(i)
    else:
        dic[i[0]] = [i]

shortest_num = 99999

def f(target, turn_num):
    global shortest_num
    if shortest_num <= turn_num:
        return

    if target == "":
        return

    if target[0] not in dic:
        return
    for i in dic[target[0]]:
        if not target.startswith(i):
            continue

        if len( target[len(i):]) == 0:
            if shortest_num > turn_num + 1:
                shortest_num = turn_num + 1
            return
        print( target[len(i):], turn_num+1)
        f( target[len(i):], turn_num+1)
        
f(T, 0)

if shortest_num == 99999:
    print(-1)
    exit()
print(shortest_num)
