N = int(input())
S = input()
Q = int(input())

temp  = "abcdefghijklmnopqrstuvwxyz"
temp_ = "abcdefghijklmnopqrstuvwxyz"

for _ in range(Q):
    c, d = map(str, input().split())
    temp = temp.replace(c, d)

dic = dict()

for num in range(len(temp_)):
    dic[temp_[num]] = temp[num]

result = ""
for s in S:
    result += dic[s]

print(result)
