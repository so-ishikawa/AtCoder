"""
#文字列として受け取るとき
A, B, C = input().split()

A, B = map(int, input().split())

#list型で取得
l = list(map(int, input().split()))
"""
N, X = map(int, input().split())
A_list = list(map(int, input().split()))
B_set = set(A_list)


# A_list.sort()
if X == 0:
    print("Yes")
    exit()

for i in A_list:
    if (i + X) in B_set:
        print("Yes")
        exit()
print("No")

# a = [3,5,6,8,13,18,20]


