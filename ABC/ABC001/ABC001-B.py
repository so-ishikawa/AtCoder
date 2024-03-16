m = int(input())
temp = m / 1000
if 0.1 > temp:
    print("00")
    exit()
if 0.1 <= temp <= 5:
    print(str(int(temp*10)).zfill(2))
    exit()
if 6 <= temp <= 30:
    print(str(int(temp+50)).zfill(2))
    exit()
if 35 <= temp <= 70:
    print(str(int((temp-30)/5+80)).zfill(2))
    exit()
print(89)
