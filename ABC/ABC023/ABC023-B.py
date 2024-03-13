N = int(input())
S = input()

set_ = set()
temp = "b"

set_.add(temp)

for i in range(1, N):
    if i % 3 == 1:
        temp = "a" + temp + "c"
        set_.add(temp)
        continue
    if i % 3 == 2:
        temp = "c" + temp + "a"
        set_.add(temp)
        continue
    if i % 3 == 0:
        temp = "b" + temp + "b"
        set_.add(temp)
        continue

if S in set_:
    print((len(S) - 1 )//2)
    exit()

print(-1)
