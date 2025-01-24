import math
R = int(input())

if R < math.sqrt(2)/2:
    print(0)
    exit()

R_ = R - math.sqrt(2)/2
naname_num = R_ // math.sqrt(2)

R_ = R - 1/2
xy_num = int(R_)
if R < math.sqrt((xy_num + 1/2)**2 + (1/2)**2):
    xy_num -= 1

count = 0
for i in range(2, xy_num+1):
    h = 0.5
    if R < math.sqrt(h**2 + (i+0.5)**2):
        continue
    while h <= i-0.5:
        h += 1
        if R < math.sqrt(h**2 + (i+0.5)**2):
            break
        count += 1

print(int(naname_num*4 + xy_num*4+1+count*8))
        
        
