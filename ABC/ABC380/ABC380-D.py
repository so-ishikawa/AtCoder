


S = input()
Q = int(input())
K_list = list(map(int, input().split()))

def get_target_char(S, K_num):

    _K_num = K_num % len(S)
    return(S[_K_num])

def get_double_count(S, K_num):
    s_length = len(S)
    while K_num >= s_length:
        s_length *= 2

    block_count = s_length // len(S)
    count = 0
    while block_count > 2:
        K_num = K_num % block_count
        block_count = block_count // 2
        count += 1
    if K_num < len(S):
        if (-1)**count == -1:
            return(not True)
        return(True)
    
    if (-1)**count == -1:
        return(not False)
    return(False)

    



for i in K_list:
    i = i-1
    state = get_double_count(S, i)
    char = get_target_char(S, i)
    if state:
        print(char, end=" ")
        continue
    print(char.swapcase(), end=" ")
