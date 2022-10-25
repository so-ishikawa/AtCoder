N, x, y = map(int, input().split())
# A_list = list(map(int, input().split()))
"""
3 -1 1
2 1 3
"""
A_list = [2, 3]

# -3 * 2 < index <3 * 2
dp = [False] * 13
dp[6] = True

nxtdp = [False] * 13

for j in range(len(dp)):
    if dp[j]:
        
