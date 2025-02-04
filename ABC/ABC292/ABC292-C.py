import math
N = int(input())

dic = dict()

for i in range(1, N):
    temp = []
    for j in range(1,  int(math.sqrt(i))+1):
        if i % j == 0:
            temp.append(j)
            if j != i//j:
                temp.append(i//j)
    dic[i] = len(temp)

count = 0
for i in range(1, N):
    count += (dic[i] * dic[N-i])
    
print(count)
