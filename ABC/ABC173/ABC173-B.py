N = int(input())
dic = dict({"AC":0, "WA":0, "TLE":0, "RE":0})

for i in range(N):
    s = input()
    dic[s] = dic[s] + 1

print("AC x %s" % dic["AC"])
print("WA x %s" % dic["WA"])
print("TLE x %s" % dic["TLE"])
print("RE x %s" % dic["RE"])
