N, K, X = map(int, input().split())
A_list = list(map(int, input().split()))

count = 0
for i in A_list:
    count += (i//X)

if count >= K:
    print(sum(A_list)-K*X)
    exit()

for i in range(len(A_list)):
    num = A_list[i] // X
    A_list[i] = A_list[i] - num*X

K_ = K - count

A_list.sort(reverse=True)
print(sum(A_list[K_:]))

