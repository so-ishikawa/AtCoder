N = int(input())
A_list = list(map(int, input().split()))


a = "ABCDEFCGHI"
dict_ = dict()
list_ = []
count = 0
diff = 0


for i in a:
    if i not in dict_:
        dict_[i] = count
        count += 1
        list_.append(i)
        continue
    old_key = dict_[i]
    del list_[:old_key+1]
    print(dict_, list_)
    break



exit()



check_list = [False]*N

for i in range(len(A_list)-1):
    if A_list[i] == A_list[i+1]:
        check_list[i] = True

count = 0
temp_set = set()

# even
for i in range(0, len(check_list), 2):
    if not check_list[i]:
        count = 0
        temp_set.clear()
        continue

    if A_list[i] in temp_set:
        pass
        



# odd
for i in range(1, len(check_list), 2):
    pass
