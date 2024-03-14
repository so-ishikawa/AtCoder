s = input()

last_count = 0
last_char = ""

result = ""

for s_ in s:
    if s_ == last_char:
        last_count += 1
        continue
    if last_char != "":
        result = result + last_char + str(last_count)

    last_char = s_
    last_count = 1
    
result = result + last_char + str(last_count)

print(result)
