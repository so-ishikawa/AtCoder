N, M = map(int, input().split())
w_list = list(map(int, input().split()))
# N = 10
# M = 100

masu = []
for n in range(N+1):
    masu.append([[]]*(M+1))

