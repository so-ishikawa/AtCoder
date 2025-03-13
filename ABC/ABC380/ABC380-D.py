S = input()
Q = int(input())
K_list = list(map(int, input().split()))

for i in K_list:
    char = S[(i % len(S))-1]

    group_num = i // len(S)
    if i % len(S) != 0:
        group_num += 1

    group_num_0index = group_num - 1
    if group_num_0index.bit_count() % 2 == 1:
        char = char.swapcase()
    print(char, end=" ")
