import sys
A, B, C, D, E = map(int, input().split())

temp_list = [A,B,C,D,E]
temp = set(temp_list)
if len(temp) != 2:
    print("No")
    sys.exit(0)

if temp_list.count(A) == 2 or temp_list.count(A) == 3:
    print("Yes")
    sys.exit(0)

print("No")
