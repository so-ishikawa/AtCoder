N, K = map(int, input().split())

temp = 0

for n in range(1, N+1):
    temp = temp + n*100*K + (K*(K+1))//2
print(temp)
