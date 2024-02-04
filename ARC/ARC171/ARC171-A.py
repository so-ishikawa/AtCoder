import math
T = int(input())
for i in range(T):
    N, A, B = map(int, input().split())
    if N < A:
        print("No")
        continue
    if N // 2 <= A:
        # ok case
        if (N-A)**2 >= B and N >= A:
            print("Yes")
            continue
        else:
            print("No")
            continue
    else:
        # out case
        key_value = int(math.ceil(N/2)) 
        space_in_blank = N * key_value
        capable_space = space_in_blank - key_value*A
        if capable_space >= B:
            print("Yes")
            continue
        else:
            print("No")
            continue
