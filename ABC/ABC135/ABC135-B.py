N = int(input())
p_list = list(map(int, input().split()))
p_list.insert(0, "dummy")

count = 0
for i in range(1, N+1):
    if i != p_list[i]:
        count += 1
if count == 2 or count == 0:
    print("YES")
    exit()
    
print("NO")
