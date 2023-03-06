S, T, X = map(int, input().split())
if S < T:
    if S <= X and X < T:
        print("Yes")
    else:
        print("No")
else:
    if 0 <= X and X < T or S <= X and X < 24:
        print("Yes")
    else:
        print("No")
