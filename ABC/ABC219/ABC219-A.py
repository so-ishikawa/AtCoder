import sys

X = int(input())
next_border = 0
if 0 <= X and X < 40:
    next_border = 40
elif 40 <= X and X < 70:
    next_border = 70
elif 70 <= X and X < 90:
    next_border = 90
else:
    print("expert")
    sys.exit(0)
print(next_border - X)
