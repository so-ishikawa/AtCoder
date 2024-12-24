N = int(input())
S = input()

temp = []
last = ""
for s in S:
    if last != s:
        temp.append(s)
        last = s
print(len(temp))
