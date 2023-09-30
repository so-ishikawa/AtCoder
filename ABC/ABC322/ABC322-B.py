N, M = map(int, input().split())
S = input()
T = input()

p_flag = False
s_flag = False

if T[:len(S)] == S:
    p_flag = True

if T[-len(S):] == S:
    s_flag = True

if p_flag == True and s_flag == True:
    print(0)
    exit()

if p_flag == True and s_flag == False:
    print(1)
    exit()

if p_flag == False and s_flag == True:
    print(2)
    exit()

if p_flag == False and s_flag == False:
    print(3)
    exit()

