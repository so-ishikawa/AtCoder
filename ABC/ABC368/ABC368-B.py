N = int(input())
A_list = list(map(int, input().split()))



count = 0
while True:
    count += 1
    A_list.sort(reverse=True)
    A_list[0] = A_list[0]-1
    A_list[1] = A_list[1]-1
    if len([x for x in A_list if x > 0]) <= 1:
    	break
print(count)