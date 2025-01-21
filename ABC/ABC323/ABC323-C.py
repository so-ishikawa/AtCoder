N, M = map(int ,input().split())
A_list = list(map(int, input().split()))
S_list = []
for i in range(N):
    S_list.append(input())

Score_list = []
for i_index in range(len(S_list)):
    temp = 0
    for j_index in range(len(S_list[i_index])):
        if S_list[i_index][j_index] == "o":
            temp += A_list[j_index]
    temp += (i_index+1)
    Score_list.append(temp)


best_score = max(Score_list)


Sorted_A_list = []
for i in range(len(A_list)):
    Sorted_A_list.append((i, A_list[i]))
Sorted_A_list.sort(key=lambda x: x[1], reverse=True)


for i_index in range(len(Score_list)):
    diff = best_score - Score_list[i_index]
    if diff == 0:
        print(0)
        continue
    count = 0
    for index_score in Sorted_A_list:
        index, score = index_score
        if S_list[i_index][index] == "o":
            continue
        diff -= score
        count += 1
        if diff <= 0:
            break
    print(count)
    
    
