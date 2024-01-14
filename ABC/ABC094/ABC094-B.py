import bisect
N, M, X = map(int, input().split())
A_list = list(map(int, input().split()))

index = bisect.bisect(A_list, X)

print(min(index, len(A_list)-index))
