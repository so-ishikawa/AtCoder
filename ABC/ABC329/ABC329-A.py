S = input()
for i in range(len(S)):
    if i == len(S)-1:
        print(S[i])
        exit()
    print(S[i], end=" ")
