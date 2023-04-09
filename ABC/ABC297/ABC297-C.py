"""
A, B = map(int, input().split())
#list型で取得
l = list(map(int, input().split()))
"""
H, W = map(int, input().split())
for _ in range(H):
    s = input()
    print(s.replace("TT","PC"))
