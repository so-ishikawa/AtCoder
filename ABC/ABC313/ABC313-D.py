N, K = map(int, input().split())

result = [None]*N
result.insert(0, "dummy")

for i in range(1, N+1, K):
    cmd = "? "
    for j in range(K):
        cmd = cmd + str(i+j)
        if j != K-1:
            cmd += " "
    
