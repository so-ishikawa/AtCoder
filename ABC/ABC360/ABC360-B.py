S, T = map(str, input().split())
for i in range(1, len(S)-1):
    temp = ""
    for j in range(i-1, len(S), i):
        temp += S[j]
    # print(temp)
    if temp == T:
        print("Yes")
        exit()
print("No")
