N, K = map(int, input().split())
H_list = list(map(int, input().split()))

H_list.sort(reverse=True)
print(sum(H_list[K:]))
