N = int(input())
W_list = list(map(int, input().split()))

min_value = 999999999999
for i in range(N):
    temp =abs(sum(W_list[0:i])-sum(W_list[i:N]))
    if min_value > temp:
        min_value = temp
print(min_value)
    
