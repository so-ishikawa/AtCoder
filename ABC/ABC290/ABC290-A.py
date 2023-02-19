N, M = map(int, input().split())
a_list = []
b_list = []
a_list = list(map(int, input().split()))
b_list = list(map(int, input().split()))

result = 0
for i in b_list:
    result += a_list[i-1]
print(result)
