N = int(input())
current_value = N

temp = ""

while current_value != 0:
    if current_value % 2 == 0:
        current_value = current_value // 2
        temp = "B" + temp
        continue
    #else
    current_value -= 1
    temp = "A" + temp

print(temp)
