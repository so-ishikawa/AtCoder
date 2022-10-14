n = int(input())
s = input()
counter = 0
for num in range(1000):
    num_str = str(num).zfill(3)
    f1 = s.find(num_str[0], 0)
    if f1 != -1:
        # s1 = s[f1:]
        f2 = s.find(num_str[1], f1+1)
        if f2 != -1:
            # s2 = s1[f2:]
            f3 = s.find(num_str[2], f2+1)
            if f3 != -1:
                counter += 1
print(counter)
