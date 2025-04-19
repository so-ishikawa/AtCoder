#!/usr/bin/env python3
# -*- coding: utf-8-auto -*-
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import bisect
from collections import defaultdict

# 入力
N, M = map(int, input().split())

# 逆引きマップ: 材料 -> 使われているメニューのインデックス
ingredient_to_menus = defaultdict(list)
menu_list = []

for i in range(M):
    temp = list(map(int, input().split()))
    temp.pop(0)
    menu_list.append(set(temp))
    for ingredient in menu_list[-1]:
        ingredient_to_menus[ingredient].append(i)

# 材料のスケジュール
B_list = list(map(int, input().split()))
B_list.insert(0, None)  # ダミーで1-indexに合わせる

# 各メニューの「最後に使われる日」
last_day_list = [None] * M

# 後ろから順に見ていって、最後に出た日を記録
for day in range(N, 0, -1):
    b = B_list[day]
    for index in ingredient_to_menus[b]:
        if last_day_list[index] is None:
            last_day_list[index] = day

# Noneを取り除いてソート
last_day_filtered = sorted([day for day in last_day_list if day is not None])

# 各日ごとに、何個のメニューがその日以前に確定されたかを数える
for i in range(1, N + 1):
    index = bisect.bisect(last_day_filtered, i)
    print(index)

"""
import bisect

N, M = map(int, input().split())

menu_list = []
for i in range(M):
    temp = list(map(int, input().split()))
    temp.pop(0)
    menu_list.append(set(temp))

B_list = list(map(int, input().split()))
B_list.insert(0, "dummy")
#B_list.reverse()

last_day_list = [None]*(M+1)

for day in range(N, 0, -1):
    b = B_list[day]
    for index in range(len(menu_list)):
        if last_day_list[index] is not None:
            continue
        menu = menu_list[index]
        if b in menu:
            last_day_list[index] = day
last_day_list.pop()
last_day_list.sort()

for i in range(1, N+1):
    index = bisect.bisect(last_day_list, i)
    print(index)

"""
