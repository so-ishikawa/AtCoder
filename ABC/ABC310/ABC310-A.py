N, P, Q = map(int, input().split())
D_list = list(map(int, input().split()))

print(min(P,Q+min(D_list)))
