N, X = map(int, input().split())
L_list = list(map(int, input().split()))

temp = 0
temp_list = [temp]

for i in L_list:
    temp += i
    temp_list.append(temp)

print(len([x for x in temp_list if x <= X]))
