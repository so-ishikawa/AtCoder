N, K = map(int, input().split())
A_list = list(set(map(int, input().split())))

temp = sum([x for x in A_list if x <= K])
print((K*(K+1))//2 - temp)

