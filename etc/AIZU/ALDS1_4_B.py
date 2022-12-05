n = int(input())
S_list = list(map(int, input().split()))
q = int(input())
T_list = list(map(int, input().split()))

#　以下でもACだったが二分探索で解く
# print(len(set(S_list) & set(T_list)))


# 方針
# tがS_listにあるか一つずつ二分探索


counter = 0
for t in T_list:
    right = len(S_list)
    left = 0
    while left < right:

        mid = (left + right)//2
        if S_list[mid] == t:
            counter += 1
            break
        if S_list[mid] > t:
            right = mid
        else:
            left = mid + 1
    continue
print(counter)

