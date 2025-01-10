X, N = map(int, input().split())
p_set = set(map(int, input().split()))

for i in range(100):
    if X - i not in p_set:
        print(X-i)
        exit()
    if X + i not in p_set:
        print(X+i)
        exit()

