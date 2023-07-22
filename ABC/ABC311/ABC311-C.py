import sys
sys.setrecursionlimit(10000000)

N = int(input())
A_list = list(map(int, input().split()))
dic = dict()
memo_dic = set()

for i in range(1, N+1):
    dic[i] = A_list[i-1]

def f(_memo_dic, target, _pass_list):
    if target in _memo_dic:
        #loop!
        # count = 0
        """
        temp = target
        result = [temp]
        while True:
            temp = dic[temp]
            if temp == target:
                break
            result.append(temp)
        """
        # index = _pass_list.index(target)
        print(len(_pass_list) - _pass_list.index(target))
        for i in range(_pass_list.index(target), len(_pass_list)):
            print(_pass_list[i], end=" ")
        # print(dic)
        exit()

    _memo_dic_copy = _memo_dic.copy()
    _memo_dic_copy.add(target)
    _pass_list_copy = _pass_list.copy()
    _pass_list_copy.append(target)
    f(_memo_dic_copy, dic[target], _pass_list_copy)

pass_list = []
for i in range(1, N+1):
    f(memo_dic.copy(), i, pass_list.copy())
