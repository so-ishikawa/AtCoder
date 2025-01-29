import itertools

K = int(input())
l = list(range(9, 0-1,-1))

result = []
for i in range(1, 10+1):
    temp = []
    for v in itertools.combinations(l, i):
        temp.append(v)
    temp.sort()
    result += temp

# print(result)
# exit()
temp = ""
for i in result[K]:
    temp += str(i)
print(int(temp))
