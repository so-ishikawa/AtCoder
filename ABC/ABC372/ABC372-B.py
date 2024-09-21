M = int(input())
result = [None]*21
_M = M
for a in range(20, -1, -1):
    temp = 3**a
    # print(temp, _M)
    while _M >= temp:
        _M = _M - temp
        if result[a] is None:
            result[a] = 0
        result[a] = result[a] + 1

print(sum([x for x in result if x is not None]))

for i in range(len(result)):
    if result[i] is None:
        continue
    for _ in range(result[i]):
        print(i, end=" ")
