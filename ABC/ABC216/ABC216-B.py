N = int(input())
_set = set()
for i in range(N):
    s, t = map(str, input().split())
    _set.add((s, t))

print("Yes" if len(_set) != N else "No")
