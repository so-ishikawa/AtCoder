a, b, c = map(int, input().split())
temp = [a, b, c]
temp.sort()

if temp[-1] == temp[-2] + temp[-3]:
    print("Yes")
    exit()
print("No")
exit()
