N = int(input())
A_list = list(map(int, input().split()))

_set = set()
count = 0
_max = 0

index = 0 
while index < len(A_list):
    if index + 1 >= len(A_list):
        if count > _max:
            _max = count
        break
    if A_list[index] != A_list[index+1]:
        _set = set()
        if count > _max:
            _max = count
        count = 0
        index += 1
        continue

    if A_list[index] in _set:
        count = max(count-2, 0)
        _set.discard(A_list[index])
        continue

    count += 2
    if count > _max:
        _max = count
    index += 2

print(_max)
