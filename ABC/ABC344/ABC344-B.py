A_list = []
temp = -1
while temp != 0:
    _input = int(input())
    A_list.append(_input)
    temp = _input

A_list.reverse()

for i in A_list:
    print(i)
