N, M = map(int, input().split())
A_list = list(map(int, input().split()))

dic = dict()
for i in range(1, N+1):
    dic[i] = 0

max_index = 0
max_value = 0

for a_num in range(len(A_list)):
    i = A_list[a_num]

    if a_num == 0:
        max_index = i
        max_value = 1
        dic[i] = 1
        print(max_index)
        continue

    current_vote_num = dic[i] + 1
    dic[i] = current_vote_num
    if current_vote_num == max_value:
        max_value = current_vote_num
        max_index = min(max_index, i)
        print(max_index)
        continue

    if current_vote_num > max_value:
        max_value = current_vote_num
        max_index = i
        print(max_index)
        continue

    print(max_index)
        
    
