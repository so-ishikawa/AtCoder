def binary_search(num, _list):
    """
    _list����num�����݂��邩�ۂ�����
    ����: index��Ԃ� ����: False
    """
    left = 0
    right = len(_list)-1

    while True:
        mid = (left + right)//2
        if _list[mid] == num:
            return mid
        if left >= right:
            break
        if _list[mid] < num:
            left = mid + 1
        else:
            right = mid - 1
    return(False)

# print(binary_search(19, [x for x in range(20)]))
