A, B = map(int, input().split())
_max = max(A, B)
_min = min(A, B)

if _max % _min == 0:
    print(_max)
    exit()

count = 1
while _min*count < _max * _min:
    if _min*count % _max == 0:
        print(_min*count)
        exit()
    count += 1
print(_max*_min)
