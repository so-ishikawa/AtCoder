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
    _list内にnumが存在するか否かを解答
    ある: indexを返す 無い: False
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
    return(left, right)

"""
方針
S1,S2,S3,S4,S1 で宅配先がどこに入れる事が可能か
"""

print(binary_search_edit(80, [x for x in range(100) if x % 3 == 0]))



