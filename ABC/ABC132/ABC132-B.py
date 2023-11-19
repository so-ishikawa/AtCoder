n = int(input())
p_list = list(map(int, input().split()))

counter = 0
for i in range(1, len(p_list)-1):
    if p_list[i-1] <= p_list[i] and p_list[i] < p_list[i+1]:
        counter += 1
        continue
    elif p_list[i-1] > p_list[i] and p_list[i] >= p_list[i+1]:
        counter += 1
        continue
print(counter)
