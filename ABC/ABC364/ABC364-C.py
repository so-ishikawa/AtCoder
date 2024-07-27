N, X, Y = map(int, input().split())
A_list = list(map(int, input().split()))
B_list = list(map(int, input().split()))

A_list.sort(reverse=True)
B_list.sort(reverse=True)

A_sum = 0
B_sum = 0

A_count = 0
B_count = 0

for a in A_list:
    A_count += 1
    if A_sum + a > X:
        break
    A_sum += a

for b in B_list:
    B_count +=1
    if B_sum + b > Y:
        break
    B_sum += b

print(min(A_count, B_count))
