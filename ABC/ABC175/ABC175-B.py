N = int(input())
L_list = list(map(int, input().split()))
count = 0
for i in range(N-2):
    for j in range(i+1, N-1):
        for k in range(j+1, N):
            temp = set({L_list[i], L_list[j], L_list[k]})
            if len(temp) != 3:
                continue
            temp_max = max(temp)
            temp.remove(temp_max)
            temp_2 = sum(temp)
            if temp_max < temp_2:
                count += 1
print(count)
                

