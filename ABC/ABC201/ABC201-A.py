a, b, c = map(int, input().split())
temp = [a,b,c]
temp.sort()

if temp[2] - temp[1] == temp [1] - temp[0]:
    print("Yes")
else:
    print("No")
