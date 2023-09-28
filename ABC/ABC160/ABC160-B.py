X = int(input())

count_500 = X // 500 
res_500 = X % 500

count_5 = res_500 // 5
print(count_500*1000 + 5*count_5)
