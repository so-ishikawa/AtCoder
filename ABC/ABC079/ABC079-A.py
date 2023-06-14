N = input()
if len(set(N)) == 1:
    print("Yes")
    exit()

if len(set(N)) == 2:
    if N.count(N[0]) == 1 or N.count(N[-1]) == 1:
        print("Yes")
        exit()

print("No")
exit()
