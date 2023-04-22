"""
A, B = map(int, input().split())
#list型で取得
l = list(map(int, input().split()))
"""
N = int(input())
S = input()

max_length = 0
current_length = 0
for i in S:
    if i == "o":
        current_length += 1
        if current_length > max_length:
            max_length = current_length
        continue
    else:
        current_length = 0

if max_length == N or max_length == 0:
    print(-1)
else:
    print(max_length)

        
