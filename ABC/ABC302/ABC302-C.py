import copy
N, M = map(int, input().split())
S_list = []
for i in range(N):
    S_list.append(input())

# S_list.sort()

def diff_1(str0, str1):
    list0 = list(str0)
    list1 = list(str1)
    list0.sort()
    list1.sort()
    if list0 == list1:
        return False
    
    for i in range(M):
        for j in range(M):
            if str0[:i] + str0[i+1:] == str1[:j] + str1[j+1:]:
                return True
    return False

def f(_flag_list, S):
    for index in range(len(_flag_list)):
        
        if _flag_list[index] == False:
            continue


        str0 = S_list[index]
        str1 = S
        
        if diff_1(str0, str1):

            _flag_list[index] = False

            if True not in _flag_list:
                print("Yes")
                exit()

            f(copy.copy(_flag_list), S_list[index])


    

for index in range(len(S_list)):
    flag_list = [True] * N
    flag_list[index] = False

    f(copy.copy(flag_list), S_list[index])

print("No")
