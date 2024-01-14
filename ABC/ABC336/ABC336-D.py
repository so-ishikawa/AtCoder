N = int(input())
A_list = list(map(int, input().split()))

temp = [None]*N

def set_pyramid(target, padding, hight):
    flag = False
    count = 0
    for i in range(len(target)):
        if count == 1 and flag:
            return
        if padding > i:
            continue
        if count == hight:
            flag = True
            count -= 1
        elif flag:
            count -= 1
        else:
            count += 1
        if count == 0:
            return
        target[i] = count


# set_pyramid(temp, 2, 2)
# print(temp)

min_value = 999999999999999
for i in range(((N+1)//2), 0, -1):#hight
    
    if (i * 2 -1) == N:
        set_pyramid(temp, 0, i)
        for k in range(N):
            if A_list[k] < temp[k]:
                break
        v = 0
        for k in range(N):
            v += (A_list[k] - temp[k])
        if min_value > v:
            min_vlaue = v
        temp = [None]*N
        continue
    for j in range((N - (i*2-1))+1):
        # print(i, j)
        set_pyramid(temp, j, i)
        flag = False
        v = 0
        for k in range(N):
            # print(temp)
            if temp[k] == None:
                continue
            if A_list[k] < temp[k]:
                flag = True
                break
            v += (A_list[k]-temp[k])
        v += (N - (2*i-1))
        if flag:
            temp = [None]*N
            continue
        if min_value > v:
            min_vlaue = v
        
        temp = [None]*N
print(min_value)
