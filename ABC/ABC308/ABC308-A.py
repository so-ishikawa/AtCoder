S = list(map(int, input().split()))
if not(S[0] <= S[1] and S[1] <= S[2] and S[2] <= S[3] and S[3] <= S[4] and S[4] <= S[5] and S[5] <= S[6] and S[6] <= S[7]):
    print("No")
    exit()

temp = [x for x in S if x >= 100 and x <= 675]
if len(temp) != 8:
    print("No")
    exit()

temp = [x for x in S if x % 25 == 0]
if len(temp) != 8:
    print("No")
    exit()
print("Yes")
exit()
 
