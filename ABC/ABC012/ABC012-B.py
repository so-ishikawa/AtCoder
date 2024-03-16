N = int(input())
print("%s:%s:%s" % (str(N//3600).zfill(2), str(N%3600//60).zfill(2), str(N%3600%60).zfill(2)))

