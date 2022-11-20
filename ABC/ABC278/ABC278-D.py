N = int(input())
A_list = list(map(int, input().split()))
Q = int(input())

query_list = []
for i in range(Q):
    query = list(map(int, input().split()))
    query_list.append(query)

"""方針
全てのA_listに数字を操作するようなことはしない　※重すぎる

1の命令が来たら辞書の内容を全破棄　common_valueの更新
2の命令が来たら個々の更新内容を辞書に登録
3の命令が来たら辞書の内容とcommon_valueの内容から出力
"""

common_value = 0
dic = {}

# 一度でもquery 1が来ていたらTrue
delete_flag = False

for i in query_list:
    if i[0] == 1:
        delete_flag = True
        dic.clear()
        common_value = i[1]
    elif i[0] == 2:
        if i[1] in dic:
            dic[i[1]] += i[2]
        else:
            dic[i[1]] = i[2]
    else:
        # 3
        if delete_flag:
            if i[1] in dic:
                print(common_value + dic[i[1]])
            else:
                print(common_value)
        else:
            if i[1] in dic:
                print(A_list[i[1]-1] + dic[i[1]])
            else:
                print(A_list[i[1]-1])

