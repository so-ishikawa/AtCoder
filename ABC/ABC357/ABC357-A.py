N, M = map(int, input().split())
H_list= list(map(int, input().split()))

temp = M
count = 0
for h in H_list:
    if M - h < 0:
        print(count)
        exit()
    M = M - h
    count += 1
print(count)

