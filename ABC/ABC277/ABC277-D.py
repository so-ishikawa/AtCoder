N, M = map(int, input().split())
A_list = list(map(int, input().split()))

min_value = 9999999999

def f(i, temp):
    global min_value

    if i not in temp and (i+1)%M not in temp:
        if min_value > sum(temp):
            min_value = sum(temp)
    print(min_value)
    if i in temp:
        temp2 = temp
        temp2.remove(i)
        f(i, temp2)

    if (i+1)%M in temp:
        temp3 = temp
        temp3.remove((i+1)%M)
        f((i+1)%M, temp3)

for i in A_list:
    temp = A_list
    temp.remove(i)
    f(i, temp)

print(min_value)
