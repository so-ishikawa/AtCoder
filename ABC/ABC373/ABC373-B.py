key_dic = dict()

S = input()
for i in range(len(S)):
    key_dic[S[i]] = i

temp = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
sum_ = 0
for i in range(25):
    sum_ += abs(key_dic[temp[i]] - key_dic[temp[i+1]])
print(sum_)
