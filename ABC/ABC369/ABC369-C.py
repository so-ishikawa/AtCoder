N = int(input())
A_list = list(map(int, input().split()))

sum_ = 0
sum_ += len(A_list) #1
sum_ += (len(A_list)-1)#2

diff_list = []

for i in range(len(A_list)-1):
    temp = A_list[i+1]-A_list[i]
    diff_list.append(temp)

current_index = 0
combo = 0
pre_value = 0
diff_value = 0
for i in diff_list:
    if combo == 0:
        combo = 1
        pre_value = i
        continue
    if combo == 1:
        combo = 2
        diff_value = i - pre_value
        pre_value = i
        continue
    if i - pre_value != diff_value:
        if combo > 2:
            sum_ += (combo*(combo-1)//2)
        pre_value = i
        combo = 0
        diff_value = 0
        continue
    combo += 1

print(sum_)
