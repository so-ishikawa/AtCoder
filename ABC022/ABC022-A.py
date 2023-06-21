N, S, T = map(int, input().split())
W = int(input())
A_list = []
for i in range(N-1):
    A_list.append(int(input()))

temp = W
count = 0
if S <= temp and temp <= T:
    count += 1

for i in A_list:
    temp += i
    if S <= temp and temp <= T:
        count += 1
    
print(count)
