import itertools

N, M = map(int, input().split())
S_list = []
for i in range(N):
    s = input()
    S_list.append(s)

S_list_bin = []
for i in range(N):
    temp = ""
    for j in range(M):
        if S_list[i][j] == "o":
            temp += "1"
        else:
            temp += "0"
    temp = int(temp,2)
    S_list_bin.append(temp)

counter = 0
good = int("1"*M,2)
for i in itertools.combinations(range(N),2):
    #print(bin(S_list_bin[i[0]]), bin(S_list_bin[i[1]]))
    if (S_list_bin[i[0]] | S_list_bin[i[1]]) == good:
        counter += 1
print(counter)
