N, M, K = map(int, input().split())
A_list = list(map(int, input().split()))

temp = []
for i in range(len(A_list)):
    temp.append((i+1, A_list[i]))

result = [None]*len(A_list)

temp.sort(key=lambda x: -x[1])
temp.insert(0, "dummy")

remain = K - sum(A_list)

# print(temp, remain)
for i in range(len(temp)):
    if i == 0:
        continue
    if i <= M:
        #winner side
        # _sum = 0
        # rival_num = (M+1 - i+1) + 1
        
        # current_remain = remain
        # current_temp = temp[i][1]
        flag = False
        for _remain in range(remain+1):
            _sum = 0
            current_temp = temp[i][1] + _remain
            
            for j in range(i+1, (M+1)+1):
                _sum += (current_temp - temp[j][1])

            if current_temp < _sum and _remain == 0:
                result[temp[i][0]-1] = 0
                continue

            if remain - _remain < _sum:
                

        

        
    else:
        #loser side
        pass

print(result)
