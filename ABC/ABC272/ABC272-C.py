N = int(input())
A_list = list(map(int, input().split()))
A_list.sort()
even_list = [i for i in A_list if i % 2 == 0]
odd_list = [i for i in A_list if i % 2 != 0]

even_max_value = 0
odd_max_value = 0
if len(even_list) >= 2:
    even_max_value = even_list[len(even_list)-1] + even_list[len(even_list)-2]
if len(odd_list) >= 2:
    odd_max_value = odd_list[len(odd_list)-1] + odd_list[len(odd_list)-2]

if even_max_value == 0 and odd_max_value == 0:
    print(-1)
else:
    if even_max_value > odd_max_value:
        print(even_max_value)
    else:
        print(odd_max_value)
