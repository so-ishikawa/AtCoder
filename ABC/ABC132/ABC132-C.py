N = int(input())
d_list = list(map(int, input().split()))

d_list.sort()

print(d_list[len(d_list)//2] - d_list[len(d_list)//2-1])
