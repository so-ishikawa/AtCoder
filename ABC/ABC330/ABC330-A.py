N, L = map(int, input().split())
A_list = list(map(int, input().split()))

print(len([x for x in A_list if x >= L]))
