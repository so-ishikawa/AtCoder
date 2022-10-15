n = int(input())
a_list = list(map(int, input().split()))
# a_list.sort()
kind_list = a_list
kind_list = list(set(kind_list))
kind_list.sort()

result = [0] * n

# for N in range(n):
# counter = 0
for i in a_list:
    index = kind_list.index(i)
    next_index = index + 1
    while True:
        if next_index == len(kind_list) or i != kind_list[next_index]:
            break
        next_index += 1
    if len(kind_list) - next_index == N:
        # counter += 1
        result 
print(counter)
