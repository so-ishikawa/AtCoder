"""
#str型で受け取るとき
s = input()
#int型で受け取るとき
s = int(input())
A, B = map(int, input().split())
#list型で取得
l = list(map(int, input().split()))
"""
N = int(input())
x_list = list(map(int, input().split()))
x_list.sort()
print(sum(x_list[N:-1*N])/len(x_list[N:-1*N]))

