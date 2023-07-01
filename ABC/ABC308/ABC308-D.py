import sys
sys.setrecursionlimit(10**8)


H, W = map(int, input().split())
S_list = []
for _ in range(H):
    S_list.append(input())


word_dic = {"s":"n", "n":"u", "u":"k", "k":"e", "e":"s"}

def f(current, _dic, word):
    if current == (H-1, W-1):
        print("Yes")
        exit()
    h = current[0]
    w = current[1]
    if h + 1 <= H - 1:
        if (h+1, w) not in _dic and S_list[h+1][w] == word_dic[word]:
            _dic[(h+1, w)] = ""
            f((h+1, w), _dic, word_dic[word])

    if h - 1 >= 0:
        if (h-1, w) not in _dic and S_list[h-1][w] == word_dic[word]:
            _dic[(h-1, w)] = ""
            f((h-1, w), _dic, word_dic[word])

    if w + 1 <= W - 1:
        if (h, w+1) not in _dic and S_list[h][w+1] == word_dic[word]:
            _dic[(h, w+1)] = ""
            f((h, w+1), _dic,  word_dic[word])

    if w - 1 >= 0:
        if (h, w-1) not in _dic and S_list[h][w-1] == word_dic[word]:
            _dic[(h, w-1)] = ""
            f((h, w-1), _dic,  word_dic[word])

dic = dict()
dic[(0,0)] = ""
f((0, 0), dic, "s")
print("No")
