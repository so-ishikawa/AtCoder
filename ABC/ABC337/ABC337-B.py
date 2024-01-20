S = input()

for a in range(101):
    for b in range(101):
        for c in range(101):
            temp = "A"*a + "B"*b + "C"*c
            if temp == S:
                print("Yes")
                exit()
print("No")
exit()
