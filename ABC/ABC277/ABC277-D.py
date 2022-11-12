N, M = map(int, input().split())
A_list = list(map(int, input().split()))

dic = {}
for i in A_list:
    if i not in dic:
        dic[i] = 1
    else:
        dic[i] += 1

min_value = 99999999999

for i in A_list:
    temp = A_list
    num = i

    _dic = dic.copy()
    _dic.pop(num)
    while (num+1)%M in _dic:
        _dic.pop((num+1)%M)
        num = (num+1)%M
    result = 0
    for key, value in _dic.items():
        result += key*value
    if result < min_value:
        min_value = result

print(min_value)
