import bisect

N, K = map(int, input().split())
h_list = list(map(int, input().split()))

h_list.sort()

print(len(h_list) - bisect.bisect_right(h_list, K))
