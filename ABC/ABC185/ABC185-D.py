N, M = map(int, input().split())
if M == 0:
    print(1)
    exit()

A_list = []

if M != 0:
    A_list = list(map(int, input().split()))

#add dummy
A_list.append(0)
A_list.append(N+1)

A_list.sort()

W_list = []

if N == M:
    print(0)
    exit()



for i in range(len(A_list)-1):
    temp = A_list[i+1] - A_list[i] - 1
    if temp == 0:
        continue
    W_list.append(temp)


stump_size = min(W_list)

stump_count = 0

for i in W_list:
    if i % stump_size == 0:
        stump_count += i//stump_size
        continue
    else:
        stump_count += (i//stump_size + 1)

print(stump_count)
