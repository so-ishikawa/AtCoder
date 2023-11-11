N, X = map(int, input().split())
S_list = list(map(int, input().split()))

temp = [x for x in S_list if X >= x]
print(sum(temp))
