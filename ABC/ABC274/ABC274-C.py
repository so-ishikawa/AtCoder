N = int(input())
A_list = list(map(int, input().split()))

result = [None]*(2*N+1+1)
result[1] = 0

for index in range(len(A_list)):
    i = index + 1
    gen = result[A_list[index]]
    result[2*i] = gen+1
    result[2*i+1] = gen+1
    # print(result)

for i in range(1, len(result)):
    print(result[i])
