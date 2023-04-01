"""
#文字列として受け取るとき
A, B, C = input().split()

A, B = map(int, input().split())

#list型で取得
l = list(map(int, input().split()))
"""
# s_list = []
for i in range(8):
    s = input()
    temp = s.find("*")
    if temp == -1:
        continue
    print("abcdefgh"[temp]+str(8 - i))
    exit()
    # s_list.append(input())


