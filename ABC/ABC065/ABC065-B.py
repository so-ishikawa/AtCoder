N = int(input())
dic = dict()
exists = set()

for i in range(1, N+1):
    dic[i] = int(input())

temp = 1
exists.add(1)
count = 0
while True:
    temp = dic[temp]
    count += 1
    if temp in exists:
        print(-1)
        exit()
    if temp == 2:
        print(count)
        exit()
    exists.add(temp)
