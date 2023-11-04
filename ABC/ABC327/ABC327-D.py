N, M = map(int, input().split())
A_list = list(map(int, input().split()))
B_list = list(map(int, input().split()))

A_list.insert(0, "dummy")
B_list.insert(0, "dummy")

temp = [None] * (N+1)

def f(index, _temp):
    print(index, _temp)
    a_index = A_list[index]
    b_index = B_list[index]
    a = _temp[a_index]
    b = _temp[b_index]

    if a == 0 and b == 0:
        return
    elif a == 1 and b == 1:
        return

    if index == M:
        print("Yes")
        exit()
        
    if a == None and b == None:
        a_temp = _temp.copy()
        a_temp[a_index] = 0
        a_temp[b_index] = 1
        f(index + 1, a_temp)
        b_temp = _temp.copy()
        b_temp[a_index] = 1
        b_temp[b_index] = 0
        f(index + 1, b_temp)
    elif a == 0 and b == 1:
        f(index+1, _temp.copy())
    elif a == 1 and b == 0:
        f(index+1, _temp.copy())
    elif a == None and b == 0:
        a_temp = _temp.copy()
        a_temp[a_index] = 1
        # a_temp[b_index] = 0
        f(index + 1, a_temp)
    elif a == None and b == 1:
        a_temp = _temp.copy()
        a_temp[a_index] = 0
        # a_temp[b_index] = 1
        f(index + 1, a_temp)
    elif a == 0 and b == None:
        a_temp = _temp.copy()
        # a_temp[a_index] = 0
        a_temp[b_index] = 1
        f(index + 1, a_temp)
    elif a == 1 and b == None:
        a_temp = _temp.copy()
        # a_temp[a_index] = 0
        a_temp[b_index] = 0
        f(index + 1, a_temp)




f(1, temp.copy())

print("No")
