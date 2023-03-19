N = int(input())
a_list = list(map(int, input().split()))
temp_list = [x for x in a_list if x % 2 == 0]
for i in temp_list:
    print(i, end=' ')
