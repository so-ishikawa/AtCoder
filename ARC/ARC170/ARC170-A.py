N = int(input())
S = input()
T = input()

S_bit = S.replace("A", "0")
S_bit = S_bit.replace("B", "1")

T_bit = T.replace("A", "0")
T_bit = T_bit.replace("B", "1")

S_num = int("0b" + S_bit, 0)
T_num = int("0b" + T_bit, 0)

# count = 0
min_count = 999999999999999999999999999
def f(_S_num, _count, _b_index):
    global T_num
    global min_count
    for b_index in range(_b_index+1, N-1):
        #S:A T:A in right side
        if (not(_S_num & (1<<b_index))) == (not (T_num & (1<<b_index))):
            continue
        #S:B T:B
        if (_S_num & (1<<b_index)) == (T_num & (1<<b_index)):
            for a_index in range(b_index+1, N):
                #S:A T:A or S:B T:B case
                if (_S_num & (1<<a_index)) == (T_num & (1<<a_index)):
                    continue
                if (_S_num & (1<<a_index)) and (not(T_num & (1<<a_index))):
                    _S_num |= (1<<b_index)
                    _S_num &= ~(1<<a_index)
                    _count += 1
                    f(_S_num, _count, b_index)
                    break
                if a_index == N-1:
                    if _S_num != T_num:
                        print(-1)
                        exit()
                else:
                    if min_count > _count:
                        min_count = _count
        elif (_S_num & (1<<b_index)) and (not(T_num & (1<<b_index))): #S:B #T:A in rightside case
            print(-1)
            exit()
        else:
            for a_index in range(b_index+1, N):
                if (_S_num & (1<<a_index)) == (T_num & (1<<a_index)):
                    continue
                if (_S_num & (1<<a_index)) and (not(T_num & (1<<a_index))):
                    _S_num |= (1<<b_index)
                    _S_num &= ~(1<<a_index)
                    _count += 1
                    f(_S_num, _count, b_index)
                    break
                if a_index == N-1:
                    if S_num != T_num:
                        print(-1)
                        exit()

f(S_num, 0, 0)
print(min_count)







"""
for b_index in range(N-1):
    if (S_num & (1<<b_index)) == (T_num & (1<<b_index)):
        continue
    if (S_num & (1<<b_index)) and (not(T_num & (1<<b_index))): #S:B #T:A in rightside case
        print(-1)
        exit()
    # below  S:A T:B rightside case

    for a_index in range(b_index+1, N):
        if (S_num & (1<<a_index)) == (T_num & (1<<a_index)):
            continue
        if (S_num & (1<<a_index)) and (not(T_num & (1<<a_index))):
            S_num |= (1<<b_index)
            S_num &= ~(1<<a_index)
            count += 1
            break
        if a_index == N-1:
            if S_num != T_num:
                print(-1)
                exit()
print(count)
"""
