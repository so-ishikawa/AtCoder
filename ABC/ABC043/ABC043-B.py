from collections import deque

d = deque()
s = input()

for _s in s:
    if _s == "0":
        d.append("0")
        continue
    if _s == "1":
        d.append("1")
        continue
    if _s == "B":
        if len(d) == 0:
            continue
        d.pop()
        continue

print("".join(d))
