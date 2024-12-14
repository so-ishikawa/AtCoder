N, K = map(int, input().split())
S = input()
print(S)
idx = [0] + [i for i in range(1,N) if S[i-1]!=S[i]] + [N]
print(idx)

# len_S = len(S)
S = S + "_"
# print((len_S))
temp = [ i for i in range(len(S)-1) if S[i] != S[i+1]]
# print(temp)
temp.append(N)
print(temp)
splited_result = []
# print(temp)
# print(S[temp[0]:temp[1]-1])
# print(S[0:1])
for index in range(len(temp)-1):
    splited_result.append(S[temp[index]:(temp[index+1])])
print(splited_result)


print(S[1:2])
