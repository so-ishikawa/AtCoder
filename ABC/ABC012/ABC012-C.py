N = int(input())
sum_ = 0
for i in range(1, 9+1):
    for j in range(1, 9+1):
        sum_ += i*j

temp = sum_ - N

ans = set()

for i in range(1, 9+1):
    t = temp / i
    if t > 9 or not(t.is_integer()):
        continue
    ans.add((i, int(t)))
    ans.add((int(t), i))

ans = list(ans)
ans.sort()

for i in ans:
    print(i[0], "x", i[1])
