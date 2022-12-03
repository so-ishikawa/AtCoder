H, W = map(int, input().split())
s_list = []
for i in range(H):
    s = input()
    s_list.append(s)
temp = 0

for i in s_list:
    temp += i.count("#")

print(temp)
