n = int(input())
a_list = list(map(int, input().split()))

dic = dict({1:0, 2:1, 3:0, 4:1, 5:2, 6:3, 7:0, 8:1, 9:0})
count = 0
for a in a_list:
    count += dic[a]
print(count)
