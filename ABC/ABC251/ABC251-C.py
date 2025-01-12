N = int(input())
set_ = set()

max_value = 0
max_index = -1

for index in  range(N):
    S, T = map(str, input().split())
    T = int(T)
    if S in set_:
        continue
    set_.add(S)

    if max_value < T:
        max_value = T
        max_index = index
print(max_index+1)
