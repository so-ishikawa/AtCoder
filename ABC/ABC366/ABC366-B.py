N = int(input())
S_list = []
max_length = 0
for _ in range(N):
    s = input()
    if max_length < len(s):
        max_length = len(s)
    S_list.append(s)

temp = []

for i in range(max_length):
    _temp = ""
    for s_no in range(len(S_list)-1, -1, -1):
        # print(s_no, "!!")
        s = S_list[s_no]
        if len(s) <= i:
            _temp += "*"
            continue
        _temp += s[i]
    temp.append(_temp)
        

for index in range(len(temp)):
    # i = temp[index]
    while True:
        if temp[index][-1:] == "*":
            temp[index] = temp[index][:-1]
            continue
        break

for i in temp:
    print(i)
            
    
