dic = dict()
dic[1] = "A"
dic[3] = "A"
dic[5] = "A"
dic[7] = "A"
dic[8] = "A"
dic[10] = "A"
dic[12] = "A"
dic[4] = "B"
dic[6] = "B"
dic[9] = "B"
dic[11] = "B"
dic[2] = "C"

x, y = map(int, input().split())
if dic[x] == dic[y]:
    print("Yes")
    exit()
print("No")
exit()
