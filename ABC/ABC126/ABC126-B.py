S = input()
pre = int(S[0:2])
aft = int(S[2:5])


pre_month_flag = False
aft_month_flag = False

if 1 <= pre <= 12:
    pre_month_flag = True
if 1 <= aft <= 12:
    aft_month_flag = True

if not pre_month_flag and aft_month_flag:
    print("YYMM")
    exit()
if pre_month_flag and not aft_month_flag:
    print("MMYY")
    exit()
if pre_month_flag and aft_month_flag:
    print("AMBIGUOUS")
    exit()
if not pre_month_flag and not aft_month_flag:
    print("NA")
    exit()
