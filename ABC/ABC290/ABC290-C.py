import sys

N, K = map(int, input().split())
a_set = set(map(int, input().split()))

for i in range(K):
    if i not in a_set:
        print(i)
        sys.exit(0)

    if i == (K-1):
        print(K)
        sys.exit(0)
