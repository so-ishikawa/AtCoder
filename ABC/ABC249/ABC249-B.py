S = input()

upper_flag = False
lower_flag = False
diff_flag = True

for i in S:
    if i.isupper():
        upper_flag = True
    if i.islower():
        lower_flag = True
    if S.count(i) != 1:
        diff_flag = False

if upper_flag and lower_flag and diff_flag:
    print("Yes")
    exit()
print("No")
exit()
