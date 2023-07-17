import itertools
S = input()

count = S.count("oxx")
pre = ["", "x", "xx"]
aft = ["", "o", "ox"]
main = ["oxx"*count]

temp = []
temp2 = []
for v in itertools.product(pre, main):
    temp.append("".join(v))

for v in itertools.product(temp, aft):
    temp2.append("".join(v))

if S in temp2:
    print("Yes")
    exit()

print("No")
exit()
