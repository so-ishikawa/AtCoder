N = int(input())
temp = []
for _ in range(N):
    temp.append(int(input()))

temp = list(set(temp))

temp.sort(reverse=True)
print(temp[1])
