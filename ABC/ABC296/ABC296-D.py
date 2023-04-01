

"""
#文字列として受け取るとき
A, B, C = input().split()

A, B = map(int, input().split())

#list型で取得
l = list(map(int, input().split()))
"""
N, M = map(int, input().split())

if N*N < M:
    print(-1)
    exit()


