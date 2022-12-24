S = int(input())
S = "%s" % S
count = S.count("00")
# print("count:", count)
#for i in range(count):
#     S = S.replace("00", "")
print(len(S)-count)
