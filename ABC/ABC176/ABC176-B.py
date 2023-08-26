N = input()
N_list = list(N)
N_list = [int(x) for x in N_list]
if sum(N_list) % 9 == 0:
    print("Yes")
    exit()
print("No")

