d = int(input())
n = int(input())
m = int(input())
d_list = []
for i in range(n-1):
    d_list.append(int(input()))
k_list = []
for i in range(m):
    k_list.append(int(input()))


def binary_search_edit(num, _list):
    """
    前後のindexを返す　
    """
    left = 0
    right = len(_list)-1

    while True:
        mid = (left + right)//2
        if _list[mid] == num:
            return mid
        if right - left <= 1:
            break
        if _list[mid] < num:
            left = mid + 1
        else:
            right = mid - 1
    if left == right:
        return(left, left+1)
    return(left, right)

"""
方針
S1,S2,S3,S4,S1 で宅配先がどこに入れる事が可能か
"""

# 最後に本店を付け加える
n = n + 1
d_list.insert(0, 0)
d_list.append(d)

sum_length = 0
for k in k_list:
    result = binary_search_edit(k, d_list)
    if len(result) == 0:
        continue
    min_length = min(abs(k - d_list[result[0]]),abs(k - d_list[result[1]]))
    print(d_list[result[0]], d_list[result[1]])
    sum_length += min_length
print(sum_length)



