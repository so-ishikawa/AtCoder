s = input()
k = int(input())
_set = set()

for i in range(len(s)):
    if not (i + k <= len(s)):
        break
    _set.add(s[i:i+k])

print(len(_set))
