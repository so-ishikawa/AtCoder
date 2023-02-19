N, K = map(int, input().split())
S = input()

result = []
count = 0
for i in S:
    if i == "o" and count < K:
        result.append("o")
        count += 1
    else:
        result.append("x")
print("".join(result))
