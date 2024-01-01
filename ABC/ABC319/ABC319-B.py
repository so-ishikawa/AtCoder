N = int(input())

def f(_list, num):
    for i in range(1, 9+1):
        if num % i == 0:
            _list.append(i)

temp = []
f(temp, N)
# print(temp)

result_str = ""
for i in range(N+1):
    _temp = []
    for j in temp:
        if i % (N // j) == 0:
            _temp.append(j)
    if len(_temp) == 0:
        result_str += "-"
    else:
        result_str += str(min(_temp))

print(result_str)
