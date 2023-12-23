N, M, X, Y = map(int, input().split())
x_list = list(map(int, input().split()))
y_list = list(map(int, input().split()))

for z in range(X+1, Y+1):
    # print(z)
    x_temp = [x for x in x_list if x >= z]
    y_temp = [y for y in y_list if y < z]
    # print(x_temp, y_temp)
    if len(x_temp) == 0 and len(y_temp) == 0:
        print("No War")
        exit()
print("War")
