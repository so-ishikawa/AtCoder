K = int(input())
A, B = map(int, input().split())

temp = B // K
# if temp == 0:
#     print("OK")
#     exit()
if temp * K >= A:
    print("OK")
else:
    print("NG")
