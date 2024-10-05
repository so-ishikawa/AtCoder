S = input()
T = input()

if S == T:
    print(0)
    exit()

if len(S) != len(T):
    if len(S) > len(T):
        T = T + "_"*(len(S)-len(T))
    else:
        S = S + "_"*(len(T)-len(S))

for i in range(len(S)):
    # print(S, T, i)
    if S[i] == T[i]:
        continue
    print(i+1)
    exit()
