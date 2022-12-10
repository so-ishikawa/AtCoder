import itertools

N, K, D = map(int, input().split())
a_list = list(map(int, input().split()))

set_ = set()
a = list(itertools.combinations(a_list,K))
for i in a:
    set_.add(sum(i))

# l = list(set_)
l = set_
l = [x for x in l if x % D == 0]
if len(l) == 0:
    print(-1)
else:
    print(max(l))
