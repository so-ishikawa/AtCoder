A, B = map(int, input().split())
count = 0
for i in range(A, B+1):
    temp = str(i)
    if temp[0] == temp[-1] and temp[1] == temp[-2]:
        count += 1
print(count)
