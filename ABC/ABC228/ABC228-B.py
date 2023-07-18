N, X = map(int, input().split())
A_list = list(map(int, input().split()))

A_list.insert(0, "dummy")
listened_list = [False] * len(A_list)

next_index = X
count = 0

while True:
    if listened_list[next_index]:
        break
    listened_list[next_index] = True
    next_index = A_list[next_index]
    count += 1

print(count)
