S = input()
T = input()

s_index = 0

for t_num in range(len(T)):
    if s_index == len(S):
        exit()
    if S[s_index] == T[t_num]:
        print(t_num+1, end=" ")
        s_index += 1
 
