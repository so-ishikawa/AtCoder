N = int(input())
A_list = []
for _ in range(N):
    a = input()
    A_list.append(a)

for i in range(N):
    for j in range(N):
        if i == j:
            continue
        if A_list[i][j] == "W" and A_list[j][i] != "L" or A_list[i][j] == "L" and A_list[j][i] != "W" or A_list[i][j] == "D" and A_list[j][i] != "D":
            print("incorrect")
            exit()
        
print("correct")
