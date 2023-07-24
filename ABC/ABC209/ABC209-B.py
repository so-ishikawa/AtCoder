N, X = map(int, input().split())
A_list = list(map(int, input().split()))

print("Yes" if X >= sum(A_list) - (len(A_list)//2) else "No")
