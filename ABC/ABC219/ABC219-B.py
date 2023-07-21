S1 = input()
S2 = input()
S3 = input()
T = input()

dic = dict()
dic[1] = S1
dic[2] = S2
dic[3] = S3

temp = ""
for i in T:
    temp += dic[int(i)]
print(temp)
