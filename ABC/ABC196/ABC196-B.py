X = input()

if "." not in X:
    print(X)
    exit()

print(X[:X.index(".")])
