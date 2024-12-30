N = int(input())
A_list = list(map(int, input().split()))
print("YES" if N == len(set(A_list)) else "NO")
