from decimal import Decimal
import math
X = input()
# X = 1
result = Decimal(X) / Decimal('10')
# print(result)
if result < 0:
    print(int(result))
    exit()
print(math.ceil(result))

