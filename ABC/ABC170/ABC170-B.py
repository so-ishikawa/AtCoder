X, Y = map(int, input().split())

turu_num = 2*X - (Y/2)
kame_num = Y/2 - X

if turu_num >=0 and kame_num >= 0 and turu_num.is_integer() and kame_num.is_integer():
    print("Yes")
    exit()
print("No")
