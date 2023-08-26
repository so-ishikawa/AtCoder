S = input()
T = input()

min_count = 99999999999999999999
for i in range(len(S)-len(T)+1):
    temp = 0
    for j in range(len(T)):
        if S[i+j] != T[j]:
            temp += 1
    if min_count > temp:
        min_count = temp
print(min_count)
