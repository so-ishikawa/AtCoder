K = int(input())

current_h = 21
current_m = 0

temp = K + current_m
carry_forward = temp // 60
if carry_forward == 1:
    current_h += 1
rest = temp % 60

print("%s:%s" % (current_h, ("%s" % (rest)).zfill(2)))

