N = int(input())
A_list = list(map(int, input().split()))

_set = set()
count = 0

# even
even_max = 0

for i in range(0, len(A_list), 2):
    if i+1 >= len(A_list):
        break
    if A_list[i] != A_list[i+1]:
        count = 0
        _set.clear()
        continue

    if A_list[i] in _set:
        # count = max(0, count-2)
        _set.discard(A_list[i])
        continue

    _set.add(A_list[i])
    count += 2
    if even_max < count:
        even_max = count

# odd
_set = set()
count = 0
odd_max = 0

for i in range(1, len(A_list), 2):
    if i+1 >= len(A_list):
        break
    if A_list[i] != A_list[i+1]:
        count = 0
        _set.clear()
        continue

    if A_list[i] in _set:
        # count = max(0, count-2)
        _set.discard(A_list[i])
        continue

    _set.add(A_list[i])
    count += 2
    if odd_max < count:
        odd_max = count

print(max(even_max, odd_max))
