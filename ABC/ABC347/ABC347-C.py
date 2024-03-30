N, A, B = map(int, input().split())
D_list = list(map(int, input().split()))

temp = set(range(1, A+B+1))
for d in D_list:
    temp.discard(d % (A+B))

temp_ = list(temp)
temp_.sort()
longest = 0

aa = 0
for i in range(len(temp_)-1):
    if temp_[i+1] - temp_[i] == 1:
        aa += 1
    else:
        aa = 0
    if aa > longest:
        longest = aa

if aa >= A:
    print("Yes")
    exit()
print("No")
