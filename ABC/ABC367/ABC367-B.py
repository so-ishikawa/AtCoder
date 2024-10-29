X = input()
while True:
    if X[-1:] == "0":
        X = X[:-1]
        continue
    if X[-1:] == ".":
        X = X[:-1]
        break
    break
if X == "":
    print(0)
    exit()
if "." in X:
    print(float(X))
    exit()
print(int(X))
        
