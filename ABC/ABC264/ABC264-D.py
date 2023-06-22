S = input()
T = "atcoder"
s = list(S)

sum_count = 0

for i in T:
    sum_count += s.index(i)
    s.remove(i)
print(sum_count)
        
