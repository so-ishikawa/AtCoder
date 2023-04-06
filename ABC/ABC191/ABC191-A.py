V, T, S, D = map(int, input().split())
if not (S*V >= D and D >= T*V):
    print("Yes")
else:
    print("No")
