A = int(input())
B = int(input())
C = int(input())
D = int(input())
E = int(input())

def ceil10(x):
    if x % 10 != 0:
        return(((x//10)+1)*10)
    return(x)


temp_list = [A, B, C, D, E]
min_value = 99999
min_index = -1
for i in range(len(temp_list)):
    _min = temp_list[i] % 10
    if _min == 0:
        continue
    if _min < min_value:
        min_value = _min
        min_index = i

if min_value == 99999:
    print(sum(temp_list))
    exit()

sum_value = 0
for i in range(len(temp_list)):
    if i == min_index:
        sum_value += temp_list[i]
        continue
    sum_value += ceil10(temp_list[i])
print(sum_value)

