X, K, D = map(int, input().split())
X = abs(X)
count = X // D
remain = X % D
can_move_count = K - count

if X >= K*D:
    print(X-K*D)
    exit()

if can_move_count % 2 == 0:
    print(remain)
    exit()

print(D-remain)
exit()
