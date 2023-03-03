a_list = list(map(int, input().split()))
pre_list = a_list.copy()

for i in range(3): #段数
    temp_list = [0] * 4
    for j in range(4): # 横行升目
        sum_ = 0
        for index in range(max(0, j-1), min(3, j+1)+1):
            sum_ += pre_list[index]
        temp_list[j] = sum_
        """
        if j == 0:
            temp_list[j] = pre_list[j] + pre_list[j+1]
        elif j == 3:
            temp_list[j] = pre_list[j-1] + pre_list[j]
        else:
            temp_list[j] = pre_list[j-1] + pre_list[j] + pre_list[j+1]
        """
    pre_list = temp_list.copy()
print(pre_list[3])
