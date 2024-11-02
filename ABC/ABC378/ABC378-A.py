A1, A2, A3, A4 = map(int, input().split())
temp = set({A1,A2,A3,A4})

if len(temp) == 4:
    print(0)
    exit()

if len(temp) == 3:
    print(1)
    exit()

if len(temp) == 2:
    _list = [A1,A2,A3,A4]
    _list.sort()
    if _list[0] != _list[1] or _list[-2] != _list[-1]:
        print(1)
        exit()
    print(2)
    exit()

if len(temp) == 1:
    print(2)
    exit()
