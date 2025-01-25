x1, y1, x2, y2 = map(int, input().split())

def f(y, x, set_):
    set_.add((y+2, x+1))
    set_.add((y+1, x+2))
    set_.add((y-1, x+2))
    set_.add((y-2, x+1))
    set_.add((y-2, x-1))
    set_.add((y-1, x-2))
    set_.add((y+1, x-2))
    set_.add((y+2, x-1))

set0 = set()
set1 = set()

f(y1, x1, set0)
f(y2, x2, set1)

if len(set0 & set1) != 0:
    print("Yes")
    exit()
print("No")
