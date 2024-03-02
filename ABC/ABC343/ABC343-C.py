import math
N = int(input())
# check 1331
# print( int(N**(1/3))+1)
max_value = 0
i = 0
while True:
    i = i + 1
    K = i**3
    if K > N:
        break
    _K = str(K)
    if _K[-1] == "0":
        continue
    flag = True
    for j in range(len(_K)//2):
        if _K[j] == _K[-1*(j+1)]:
            # print(_K[j], _K[-1*(j+1)])
            continue
        flag = False
    if flag:
        max_value = K
print(max_value)
