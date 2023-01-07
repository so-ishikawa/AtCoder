"""
#str型で受け取るとき
s = input()
#int型で受け取るとき
s = int(input())
# 入力が整数の時
A, B = map(int, input().split())
#list型で取得
l = list(map(int, input().split()))
"""
T = int(input())
test_list = []
for i in range(T):
    test_T = int(input())
    test_A_list = list(map(int, input().split()))
    test_list.append((test_T, test_A_list))

for i in range(len(test_list)):
    print(len([x for x in test_list[i][1] if x % 2 == 1]))
