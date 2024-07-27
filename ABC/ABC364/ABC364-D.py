import bisect
N, Q = map(int, input().split())
a_list = list(map(int, input().split()))

a_list.sort()
for _ in range(Q):
    b, k = map(int, input().split())
    index = bisect.bisect(a_list, b)
    aft = [x-b for x in a_list[index:index+k]]
    pre = [b-x for x in a_list[max(0,index-k):index]]  
    
    temp = aft + pre
    temp.sort()
    
    print(temp[k-1])
    
