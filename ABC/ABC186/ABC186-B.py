H, W = map(int, input().split())
block_list = []
min_value = 999999999999999999
for i in range(H):
    b = list(map(int, input().split()))
    if min_value > min(b):
        min_value = min(b)
    block_list.append(b)

total_sum = 0
for block in block_list:
    total_sum += sum([x-min_value for x in block])

print(total_sum)
