N = int(input())

temp = list(str(N))
k = len(temp)
mod2 = 0
mod1 = 0


temp_ = 0
for i in temp:
    if int(i) % 3 == 1:
        mod1 += 1
    if int(i) % 3 == 2:
        mod2 += 1
    temp_ += int(i)

if temp_ % 3 == 0:
    print(0)
    exit()
if temp_ % 3 == 1:
    if mod1 >= 1 and k > 1:
        print(1)
        exit()
    if mod2 >= 2 and k > 2:
        print(2)
        exit()
    else:
        print(-1)
        exit()
if temp_ % 3 == 2:
    if mod2 >= 1 and k > 1:
        print(1)
        exit()
    if mod1 >= 2 and k > 2:
        print(2)
        exit()
    else:
        print(-1)
        exit()
    
