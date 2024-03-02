from collections import defaultdict
N, T = map(int, input().split())

player_score_dic = defaultdict(lambda: 0)
score_kind_set = set({0})
score_num_dic =  defaultdict(lambda: 0)
score_num_dic[0] = N

for _ in range(T):
    a, b = map(int, input().split())
    old_score = player_score_dic[a]
    new_score = player_score_dic[a] + b
    score_num_dic[old_score] = score_num_dic[old_score] - 1
    score_num_dic[new_score] = score_num_dic[new_score] + 1

    score_kind_set.add(new_score)

    if score_num_dic[old_score] == 0:
        score_kind_set.discard(player_score_dic[a])

    player_score_dic[a] = new_score
    # print(score_kind_set, score_num_dic)
    print(len(score_kind_set))

        
