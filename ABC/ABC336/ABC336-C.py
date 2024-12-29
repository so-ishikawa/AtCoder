N = int(input())

dic = dict()
dic["0"] = "0"
dic["1"] = "2"
dic["2"] = "4"
dic["3"] = "6"
dic["4"] = "8"

def to_basefive(num_10):
    i = 0
    result = ""
    temp = num_10
    while num_10 >= 5**(i+1):
        i += 1
    while i >= 0:
        q = temp // 5**i
        result += str(q)
        temp = temp % 5**i
        i -= 1
    return(int(result))
    
t = to_basefive(N-1)

t = str(t)

ans = ""
for i in t:
    ans += dic[i]
print(int(ans))
