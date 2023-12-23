N = int(input())
T, A = map(int, input().split())
H_list = list(map(int, input().split()))

H_list_temp = [abs(A-(T-x*0.006)) for x in H_list]

print(H_list_temp.index(min(H_list_temp))+1)
