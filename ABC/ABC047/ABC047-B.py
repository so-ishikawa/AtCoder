W, H, N = map(int, input().split())
top = H
bottom = 0
right = W
left = 0
for _ in range(N):
    x, y, a = map(int, input().split())
    if a == 1:
        if left < x:
            left = x
        continue
    if a == 2:
        if right > x:
            right = x
        continue
    if a == 3:
        if bottom < y:
            bottom = y
        continue
    if a == 4:
        if top > y:
            top = y
        continue
    
if right - left < 0 or top - bottom < 0:
    print(0)
    exit()
# print(right, left, top, bottom)
print((right-left)*(top-bottom))
