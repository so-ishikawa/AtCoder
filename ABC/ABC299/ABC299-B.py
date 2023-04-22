"""
A, B = map(int, input().split())
#list型で取得
l = list(map(int, input().split()))
"""
N, T = map(int, input().split())
c_list = list(map(int, input().split()))
r_list = list(map(int, input().split()))

t_current_player_num = -1
t_current_player_r = -1
c1_current_player_num = 0
c1_current_player_r = r_list[0]
t_another_player_flag = False

for i in range(N):
    if T == c_list[i]:
        t_another_player_flag = True

    if t_another_player_flag:
        if c_list[i] != T:
            continue
        
        if r_list[i] > t_current_player_r:
            t_current_player_num = i
            t_current_player_r = r_list[i]
            continue
        continue

    # まだどちらか分かっていない状態
    # if c_list[i] == T and r_list[i] > t_current_player_r:
    #     t_current_player_r = r_list[i]
    #     t_current_player_num = i
    if c_list[i] == c_list[0] and r_list[i] > c1_current_player_r:
        c1_current_player_r = r_list[i]
        c1_current_player_num = i

if t_another_player_flag:
    # print("000000000000000000000")
    print(t_current_player_num+1)
else:
    # print("11111111111")
    print(c1_current_player_num+1)
