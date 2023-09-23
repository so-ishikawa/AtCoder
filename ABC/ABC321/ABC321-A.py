N = list((input()))

for i in range(len(N)-1):
    if N[i] > N[i+1]:
        continue
    print("No")
    exit()

print("Yes")
exit()
