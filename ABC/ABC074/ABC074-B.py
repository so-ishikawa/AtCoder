N = int(input())
K = int(input())
x_list = list(map(int, input().split()))

result = 0
for x in x_list:
    result += min(2*x, 2*(abs(K-x)))
print(result)
