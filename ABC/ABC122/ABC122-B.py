s = input()
max_acgt_length = 0
counter = 0

for char in s:
    if char in "ACGT":
        counter = counter + 1
        if max_acgt_length <= counter:
            max_acgt_length = counter
    else:
        counter = 0

print(max_acgt_length)
