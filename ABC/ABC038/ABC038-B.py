H1, W1 = map(int, input().split())
H2, W2 = map(int, input().split())

if len(set({H1, W1})) + len(set({H2, W2})) != len(set({H1,W1,H2,W2})):
    print("YES")
    exit()
print("NO")
