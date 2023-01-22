# 20230122 どうしても一つだけTLEが取れず
# 再帰を使うのがそもそも悪くACしている回答は見た限り全てDPだった　todo:DPで書き直す
import sys
sys.setrecursionlimit(999999999)

N, X = map(int, input().split())
A_list = []
B_list = []
for i in range(N):
    A, B = map(int, input().split())
    A_list.append(A)
    B_list.append(B)


C_list = [a * b for (a, b) in zip(A_list, B_list)]
D_list = []
for i in range(len(C_list)):
    D_list.append(sum(C_list[0:i+1]))
# print(C_list, D_list)


def f(current_x, coin_index, coin_num):
    if current_x == A_list[coin_index] * coin_num:
        # print(current_x, coin_index, coin_num)
        print("Yes")
        sys.exit(0)
    current_x = current_x - A_list[coin_index] * coin_num

    if coin_index == 0:
        return
    coin_index -= 1
    if current_x > D_list[coin_index]:
        return
    max_coin_num = min(current_x // A_list[coin_index], B_list[coin_index])
    # for i in range(max_coin_num, -1, -1):
    for i in range(max_coin_num+1):
        f(current_x, coin_index, i)


if X > sum([a * b for (a, b) in zip(A_list, B_list)]):
    print("No")
    sys.exit(0)


# for i in range(B_list[-1] + 1):
#    f(X, len(A_list)-1, i)
start_coin_num = min(X // A_list[-1], B_list[-1])
# for i in range(start_coin_num+1):
for i in range(start_coin_num, -1, -1):
    f(X, len(A_list)-1, i)

print("No")
