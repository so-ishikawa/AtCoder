n, X = map(int, input().split())
a_list = list(map(int, input().split()))

temp = bin(X)[2:]
temp = temp[::-1]

sum_ = 0
for t in range(len(temp)):
    if temp[t] == "1":
        sum_ += a_list[t]
print(sum_)
        

