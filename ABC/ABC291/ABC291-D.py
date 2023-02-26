"""
#str型で受け取るとき
s = input()
#int型で受け取るとき
s = int(input())
A, B = map(int, input().split())
#list型で取得
l = list(map(int, input().split()))
"""
import sys
sys.setrecursionlimit(10**6)

N = int(input())
a_list = []
b_list = []
for _ in range(N):
    A, B = map(int, input().split())
    a_list.append(A)
    b_list.append(B)

counter = 0

def func(index, current_num, next_num):
    global counter
    if current_num == next_num:
        return
    current_num = next_num
    index += 1
    if (index + 1) > (N-1):
        counter += 1
        return

    func(index, current_num, a_list[index+1])
    func(index, current_num, b_list[index+1])


index = 0
func(index, a_list[index], a_list[index+1])
func(index, a_list[index], b_list[index+1])
func(index, b_list[index], a_list[index+1])
func(index, b_list[index], b_list[index+1])
print(counter % 998244353)
