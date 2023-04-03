S = input()

if S[0] == "1":
    print("No")
    exit()

judge_list = []
if S[6] == "1":
    judge_list.append(1)
else:
    judge_list.append(0)

if S[3] == "1":
    judge_list.append(1)
else:
    judge_list.append(0)

if S[7] == "1" or S[1] == "1":
    judge_list.append(1)
else:
    judge_list.append(0)

if S[4] == "1": # and S[0] == "1":
    judge_list.append(1)
else:
    judge_list.append(0)

if S[8] == "1" or S[2] == "1":
    judge_list.append(1)
else:
    judge_list.append(0)

if S[5] == "1":
    judge_list.append(1)
else:
    judge_list.append(0)

if S[9] == "1":
    judge_list.append(1)
else:
    judge_list.append(0)


left_pin_flag = False
blank_pin_flag = False
right_pin_flag = False

for i in judge_list:
    if not left_pin_flag and i == 1:
        left_pin_flag = True
        continue

    if left_pin_flag and not blank_pin_flag and i == 0:
        blank_pin_flag = True
        continue

    if left_pin_flag and blank_pin_flag and not right_pin_flag and i == 1:
        print("Yes")
        exit()

print("No")
