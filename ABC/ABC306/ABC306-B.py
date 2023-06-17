A_list = list(map(int, input().split()))
temp = 0
for i in range(len(A_list)):
    temp = temp + A_list[i]* (2**(i))
print(temp)
