N = int(input())
A_list = list(map(int, input().split()))

result = [x for x in A_list if x % 2 == 0]
result = [x for x in result if not(x % 3 == 0 or x % 5 == 0)]
if result != []:
    print("DENIED")
    exit()
print("APPROVED")
