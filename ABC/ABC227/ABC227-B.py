N = int(input())
S_list = list(map(int, input().split()))

temp_set = set()

for a in range(1, 150):
    for b in range(1, 150):
        temp_set.add(4*a*b + 3*a + 3*b)

count = 0
for i in S_list:
    if i in temp_set:
        count += 1

print(N - count)


