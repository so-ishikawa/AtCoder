import bisect
X = int(input())

temp = []
for i in range(1, 1000+1):
    for j in range(2, 1000+1):
        k = i**j
        if k > 1000:
            break
        temp.append(k)
temp = list(set(temp))
temp.sort()
index = bisect.bisect(temp, X)
print(temp[index-1])
# print(temp)
