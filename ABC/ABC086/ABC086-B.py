a, b = map(int, input().split())
temp = int(str(a)+str(b))

temp = temp**(1/2)

if temp.is_integer():
    print("Yes")
    exit()
print("No")
