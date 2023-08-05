N = int(input())
A_list = list(map(int, input().split()))
A_list.sort()

ave = sum(A_list)//len(A_list)
pre_list = [x for x in A_list if ave > x]
aft_list = [x for x in A_list if ave+1 < x]

pre_diff = sum([ave- x for x in pre_list])
aft_diff = sum([x-(ave+1) for x in aft_list])
print(max(pre_diff, aft_diff))
