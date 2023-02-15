L1, R1, L2, R2 = map(int, input().split())
set_1 = set(range(L1, R1+1))
set_2 = set(range(L2, R2+1))

_len = len(set_1&set_2)
if _len != 0:
    _len = _len -1
print(_len)
