import bisect
N, K = map(int, input().split())
a_b_list = []
for i in range(N):
    a, b = map(int, input().split())
    a_b_list.append((a, b))

a_b_list.sort(key=lambda x: x[0]) #[(1, 9), (2, 5), (4, 2), (6, 3)]
all_medic = 0
for i in a_b_list:
    all_medic += i[1]

daily_medic = [all_medic]
for i in a_b_list:
    all_medic = all_medic-i[1]
    daily_medic.append(all_medic)

# print(daily_medic, K)

for i in range(len(daily_medic)):
    if daily_medic[i] <= K:
        if i==0:
            print(1)
            exit()
        print(a_b_list[i-1][0]+1)
        exit()




"""
    temp = temp + i[1]
    sum_list.append(temp)

sum_list.reverse()

index = bisect.bisect(sum_list, K)
print(sum_list, index+1)
"""
