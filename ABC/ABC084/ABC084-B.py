import re
A, B = map(int, input().split())
S = input()

result = re.match("\d{%s}-\d{%s}" % (A, B), S)
if result != None:
    print("Yes")
    exit()
print("No")
