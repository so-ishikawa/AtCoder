N, K = map(int, input().split())
A_list = list(map(int, input().split()))

seat_num = 0
sum_car = 0

for a in A_list:
    if seat_num + a > K:
        sum_car += 1
        seat_num = a
        continue
    seat_num += a

print(sum_car+1)
