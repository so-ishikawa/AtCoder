N = int(input())
T = input()

count = 0
x = 0
y = 0

for i in T:
    # print(x, y)
    if count % 4 == 0:
        if i == "S":
            x += 1
            continue
        # case: i == "R"
        count += 1
        continue
    elif count % 4 == 1:
        if i == "S":
            y -= 1
            continue
        # case: i == "R"
        count += 1
        continue
    elif count % 4 == 2:
        if i == "S":
            x -= 1
            continue
        # case: i == "R"
        count += 1
        continue
    # case: count % 4 == 3
    else:
        if i == "S":
            y += 1
            continue
        # case: i == "R"
        count += 1
        continue

print(x, y)
