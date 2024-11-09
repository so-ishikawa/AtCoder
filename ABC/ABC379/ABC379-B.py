N, K = map(int, input().split())
S = input()
result = 0
count = 0
for s in S:
    if s == "O":
        count += 1
        if count == K:
            result += 1
            count = 0
    else:
        count = 0
print(result)
            
