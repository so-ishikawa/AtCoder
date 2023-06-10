
# l = list(map(int, input().split()))
dic = dict()
dic["A"] = 0
dic["B"] = 3
dic["C"] = 4
dic["D"] = 8
dic["E"] = 9
dic["F"] = 14
dic["G"] = 23

p, q = map(str, input().split())

print(abs(dic[p]-dic[q]))
