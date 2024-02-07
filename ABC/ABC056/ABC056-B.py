W, a, b = map(int, input().split())

_a = (a + W/2)
_b = (b + W/2)

if abs(_a - _b) <= W:
    print(0)
    exit()

print( int(abs(_a - _b) -W))
