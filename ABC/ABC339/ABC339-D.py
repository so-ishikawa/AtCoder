N = int(input())
S_ban = []
for _ in range(N):
    S_ban.append(input())

player0 = None
player1 = None

for h in range(N):
    for w in range(N):
        if S_ban[h][w] == "P":
            if player0 is None:
                player0 = (h, w)
            else:
                player1 = (h, w)

direction = [(0, 1), (0, -1), (1, 0), (-1, 0)]
min_value = 99999

def f(_dir, count, _player0, _player1):
    global S_ban
    global min_value
    global direction

    if count >= 2*N:
        return
    count += 1
    _h = _player0[0] + _dir[0]
    _w = _player0[1] + _dir[1]
    if not (_h < 0 or N <= _h or _w < 0 or N <= _w or S_ban[_h][_w] == "#"):
        _player0 = (_h, _w)
        
    _h = _player1[0] + _dir[0]
    _w = _player1[1] + _dir[1]
    if not (_h < 0 or N <= _h or _w < 0 or N <= _w or S_ban[_h][_w] == "#"):
        _player1 = (_h, _w)

    if _player0 == _player1:
        if min_value > count:
            min_value = count
        return

    for dir in direction:
        f(dir, count, _player0, _player1) 


for dir in direction:
    f(dir, 0, player0, player1)

if min_value == 99999:
    print(-1)
    exit()

print(min_value)
