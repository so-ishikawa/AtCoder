"""
A, B = map(int, input().split())
#list型で取得
l = list(map(int, input().split()))
"""



N = int(input())
left = 0
right = N-1
for i in range(20-1,-1,-1):
    if right - left == 1:
        print("!", left)
    
    temp = (left + right) // 2 
    print("?", temp)
    n = int(input())

    if n == 0:
        left = temp
        
    else:
        right = temp

    if (i - 1) > (right-left):
        # 連続質問モード
        flag_1 = False
        for j in range(1,i):
            print("?", left+j)
            n_ = int(input())
            if n_ == 1 and flag_1 == False:
                flag_1 = True
                continue
            if n_ == 0 and flag_1 == True:
                
