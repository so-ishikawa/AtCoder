l1, l2, l3 = map(int, input().split())
temp = [l1, l2, l3]

if temp.count(l1) == 3:
    print(l1)
    exit()
if temp.count(l1) == 1:
    print(l1)
    exit()
if temp.count(l2) == 1:
    print(l2)
    exit()
print(l3)
exit()
