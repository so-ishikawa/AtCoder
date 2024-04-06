N = int(input())
XY_list = []
for i in range(N):
    X, Y = map(int, input().split())
    XY_list.append((X, Y))

for n in range(len(XY_list)):
    longest_length = 0
    longest_num = -1
    for t in range(len(XY_list)):
        if n == t:
            continue
        temp = ((XY_list[n][0] - XY_list[t][0])**2 + (XY_list[n][1]-XY_list[t][1])**2)**(1/2)
        if temp > longest_length:
            longest_length = temp
            longest_num = t
    print(longest_num+1)
