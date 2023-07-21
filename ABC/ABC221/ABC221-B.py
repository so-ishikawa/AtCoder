S = input()
T = input()

once_error_num = -1
for i in range(len(S)-1):
    if once_error_num == i:
        continue
    
    if S[i] != T[i]:
        if once_error_num >= 0:
            print("No")
            exit()
        if not (S[i] == T[i+1] and T[i] == S[i+1]):
            print("No")
            exit()
        once_error_num = i+1

if once_error_num == -1 and S[-1] != T[-1]:
    print("No")
    exit()

print("Yes")
exit()
