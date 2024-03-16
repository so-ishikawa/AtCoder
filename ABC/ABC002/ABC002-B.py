src = input()
src_list = list(src)
src_set = set({"a","i","u","e","o"})

temp = [x for x in src_list if x not in src_set]
print("".join(temp))
