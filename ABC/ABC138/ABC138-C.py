N = int(input())
v_list = list(map(int, input().split()))

v_list.sort()

avg = v_list[0] 
for i in range(1, len(v_list)):
    avg = (avg + v_list[i])/2
print(avg)
