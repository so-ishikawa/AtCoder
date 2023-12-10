N = int(input())
temp = 0
for _ in range(N):
    x, u = map(str, input().split())
    x = float(x)
    if u == "JPY":
        temp += x
        continue
    temp += x*380000
print(temp)
