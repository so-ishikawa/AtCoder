from itertools import permutations

N = int(input())
P_list = list(map(int, input().split()))

"""
・方針
1.一番右の数字から一つ左の数字を比較し降順になっていたら1つずれて比較する
2.昇順になっていたらその数字を含めた右側の数字で昇順になっていた数字の次に大きい
 数字を選ぶ
3.昇順になっていた数値と入れ替えて残りの数値を右から昇順にソートする
例
1.  937285146
2.  93728[5]1[4]6
3.  937284651
"""

# 1.
target_index = -1
for index in range(len(P_list)-1, -1, -1):
    if index == 0:
        # 辞書の先頭の数列が来るケースは想定していない
        assert True
    rhs_index = index
    lhs_index = index-1

    if P_list[lhs_index] < P_list[rhs_index]:
        continue
    target_index = lhs_index
    break

# 2
# 並び順を変える対象の入った一時的なlistを作成
target_value = P_list[target_index]
temp_list = P_list[target_index:len(P_list)]
temp_list.sort()

# 区切りとなる数値より一つ小さい数字を探す
current_value_index = temp_list.index(target_value)
next_small_value = temp_list[current_value_index-1]

# 次に小さい値をいったん削除し作業listの中身をソート後先頭に追加
temp_list.remove(next_small_value)
temp_list = sorted(temp_list, reverse=True)
temp_list.insert(0, next_small_value)

# 大本のlistを上書きし提出
for i in range(len(temp_list)):
    P_list[target_index+i] = temp_list[i]

for i in P_list:
    print(i, end=' ')
