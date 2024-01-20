N = int(input())
X_list = []
Y_list = []
for i in range(N):
    x, y = map(int, input().split())
    X_list.append(x)
    Y_list.append(y)

if sum(X_list) > sum(Y_list):
    print("Takahashi")
    exit()
if sum(X_list) < sum(Y_list):
    print("Aoki")
    exit()
print("Draw")
