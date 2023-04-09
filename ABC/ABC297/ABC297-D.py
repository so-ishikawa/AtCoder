"""
A, B = map(int, input().split())
#list型で取得
l = list(map(int, input().split()))
"""
A, B = map(int, input().split())
# A = 105
# B = 102
if A > B and A - B == 1:
    print(B)
    exit()
if A < B and B - A == 1:
    print(A)
    exit()

if A % 2 == 0 and B % 2 == 0 and abs(A-B) == 2:
    print(min(A,B)%2)
    exit()
if A % 2 == 1 and B % 2 == 1 and abs(A-B) ==2:
    print(int((max(A, B)-1)/2))
    exit()

count = 0
while True:
    if A == B:
        print(count)
        exit()
    if A < B:
        # print("A<B")
        B = B - A
        # print("A:",A, "B:",B)
    else:
        # print("A>B")
        A = A - B
        # print("A:",A, "B:",B)
    count += 1
