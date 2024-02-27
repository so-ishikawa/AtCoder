S = input()
T = int(input())

x_num = 0
y_num = 0
question_num = 0

for s in S:
    if s == "L":
        x_num -= 1
        continue
    if s == "R":
        x_num += 1
        continue
    if s == "U":
        y_num += 1
        continue
    if s == "D":
        y_num -= 1
        continue
    if s == "?":
        question_num += 1
        continue

if T == 1:
    print(abs(x_num) + abs(y_num) + question_num)
    exit()
if T == 2:
    _long = max(abs(x_num), abs(y_num))
    _short = min(abs(x_num), abs(y_num))
    if _long + _short <= question_num:
        if (question_num - _long - _short) % 2 == 0:
            print(0)
            exit()
        print(1)
        exit()
    if _long + _short > question_num >= _long:
        print(_long + _short - question_num)
        exit()
    print(_long - question_num + _short)
    exit()
