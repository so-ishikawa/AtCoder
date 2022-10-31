N, M = map(int, input().split())

s_list = []
for i in range(M):
    s = list(map(int, input().split()))
    s.pop(0)
    s_list.append(s)

p_list = list(map(int, input().split()))

# N is switch num
# M is light num
# p_list is odd_even list

switch_pattern_bit_list = []
for i in range(2**N):
    switch_pattern_bit_list.append(i)

light_mask_bit_list = []
for i in s_list:
    temp = 0
    for j in i:
        temp += 2**(j-1)
    light_mask_bit_list.append(temp)

temp = switch_pattern_bit_list
for light_num in range(len(light_mask_bit_list)):
    mask = light_mask_bit_list[light_num]
    temp = [temp[i] for i in range(len(temp))
            if format(temp[i] & mask, "0%sb" % N).count("1") % 2 == p_list[light_num]]

print(len(temp))

"""
    temp = [switch_pattern_bit_list[i] for i in range(len(switch_pattern_bit_list))
            if format(switch_pattern_bit_list[i] & mask, "0%sb" % N).count("1") % 2 == p_list[light_num]]
"""
