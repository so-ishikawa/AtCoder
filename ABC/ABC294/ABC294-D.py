# import numpy as np

N, Q = map(int, input().split())

# no_call_list = list(range(N, 0, -1))
no_call_num = 1
called_but_did_not_visit_set = set()

for _ in range(Q):
    i = list(map(int, input().split()))
    if i[0] == 1:
        # called = no_call_list.pop()
        # no_call_set.remove(called)
        called_but_did_not_visit_set.add(no_call_num)
        no_call_num += 1
    elif i[0] == 2:
        called_but_did_not_visit_set.discard(i[1])
    else:
        # 3
        print(min(called_but_did_not_visit_set))



