import sys

S = input()
list_s = list(S)
set_s = set(list_s)

if len(set_s) == 1:
    print(-1)
    sys.exit(0)

if len(set_s) == 2:
    if list_s.count(S[0]) == 1:
        print(S[0])
        sys.exit(0)
    elif S[0] != S[1]:
        print(S[1])
        sys.exit(0)
    else:
        print(S[2])
        sys.exit(0)

print(S[0])
