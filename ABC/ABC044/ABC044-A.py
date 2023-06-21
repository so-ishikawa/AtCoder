N = int(input())
K = int(input())
X = int(input())
Y = int(input())

if N <= K:
    print(N*X)
    exit()
print(K*X + (N-K)*Y)
