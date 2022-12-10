N, T = map(int, input().split())
a_list = list(map(int, input().split()))

sum_time = sum(a_list)
t = T % sum_time

temp = 0
for i in range(len(a_list)):
    temp += a_list[i]
    a_list[i] = temp
    if a_list[i] > t:
       temp = ((a_list[i-1]%sum_time)-t) if ((a_list[i-1]%sum_time)>t) else (t-a_list[i-1]%sum_time)
       print(i%N+1, temp)
       break



"""
# print(a_list)
for i in range(len(a_list)):
   if a_list[i] > t:
       # print(a_list[i], T)
       print(i%N+1, t - (a_list[i-1]%sum_time) )
       break
"""



"""
def binary_search(num, _list):

    left = 0
    right = len(_list)-1

    while True:
        mid = (left + right)//2
        # if _list[mid] == num:
        #     return mid
        if left >= right:
            break
        if _list[mid] < num:
            left = mid + 1
        else:
            right = mid - 1
    return(left, right)

left, right = binary_search(t, a_list)
i = 0
# print(left, right)
# if left == right:
#     i = right
# else:
i = left
# print(a_list[left], a_list[right])
print(i%N+1, t - (a_list[i-1]%sum_time))
"""
