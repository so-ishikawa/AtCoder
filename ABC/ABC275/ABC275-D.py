N = int(input())

dic = {}


def f(n):
    if n == 0:
        return 1
    if n in dic:
        return dic[n]
    result = f(n//2)+f(n//3)
    dic[n] = result
    return result


print(f(N))
