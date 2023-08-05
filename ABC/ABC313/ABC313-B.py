N, M = map(int, input().split())

winner_set = set()
loser_set = set()

for i in range(M):
    a, b = map(int, input().split())
    winner_set.add(a)
    loser_set.add(b)

result_set = winner_set - loser_set
if len(result_set) == 1:
    print(list(result_set)[0])
    exit()
else:
    print(-1)
    exit()
