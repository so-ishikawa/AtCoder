s = input()
if not s[0].isupper():
    print("No")
elif not s[len(s)-1].isupper():
    print("No")
elif not len(s[1:len(s)-1]) == 6:
    print("No")
else:
    try:
        int(s[1:len(s)-1], 10)
    except ValueError:
        print("No")
    else:
        if not (int(s[1:len(s)-1], 10) >= 100000 and int(s[1:len(s)-1], 10) <= 999999):
            print("No")
        else:
            print("Yes")
