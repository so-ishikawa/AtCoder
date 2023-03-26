a, b, c = map(int, input().split())
if len(set({a,b,c})) == 3:
    print(0)
elif len(set({a,b,c})) == 2:
    if [a, b, c].count(a) == 1:
        print(a)
    elif [a, b, c].count(b) == 1:
        print(b)
    else:
        print(c)
else:
    print(a)
