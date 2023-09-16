M = int(input())
S1 = input()
S2 = input()
S3 = input()

S1_set = set(S1)
S2_set = set(S2)
S3_set = set(S3)

target_num_list = list(S1_set & S2_set & S3_set)
if len(target_num_list) == 0:
    print(-1)
    exit()


for i in target_num_list:
    S1_num_list = []
    for num in range(S1.count(i)):
        
        S1_num_list.append
