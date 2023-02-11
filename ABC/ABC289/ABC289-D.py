"""
s = input()
#int型で受け取るとき
s = int(input())

A, B = map(int, input().split())

#list型で取得
l = list(map(int, input().split()))

"""
import sys
sys.setrecursionlimit(10 ** 9)

N = int(input())
a_list = list(map(int, input().split()))
M = int(input())
b_list = list(map(int, input().split()))
X = int(input())

from typing import List
# a = [1,2,3,4,5,6]
def binary_search(sorted_list: List[int], search_value: int) -> bool:

    left_index: int = 0
    right_index: int = len(sorted_list) - 1
    while left_index <= right_index:
        middle_index: int = (left_index + right_index) // 2
        middle_value: int = sorted_list[middle_index]

        if search_value < middle_value:
            right_index = middle_index - 1
            continue
        if search_value > middle_value:
            left_index = middle_index + 1
            continue

        return True

    return False

# print(binary_search(a, 78))
dic = {}


def func(current_step, step_len):
    next_step = current_step + step_len
    if next_step in dic:
        return
    dic[next_step] = ""
    if current_step == X:
        print("Yes")
        sys.exit(0)
    if next_step == X:
        print("Yes")
        sys.exit(0)
    if current_step > X:
        return
    if next_step > X:
        return
    if binary_search(b_list, next_step):
        return
    for i in a_list:
        if next_step + i > X:
            continue
        if next_step + i == X:
            print("Yes")
            sys.exit(0)
        func(next_step, i)

for i in a_list:
    func(0, i)
print("No")
