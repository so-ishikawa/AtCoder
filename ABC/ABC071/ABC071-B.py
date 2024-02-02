import string
S = input()

temp = set(string.ascii_lowercase)
for s in S:
    temp.discard(s)
if len(temp) == 0:
    print("None")
    exit()
print(min(temp))
