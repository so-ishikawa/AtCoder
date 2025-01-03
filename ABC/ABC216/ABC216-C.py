N = int(input())
current_value = N
current_index = 120-1
temp = [""]*120

while True:
    if current_value == 0:
        break
    if current_value % 2 == 0:
        current_value = current_value//2
        temp[current_index] = "B"
        current_index -= 1
        continue
    #else
    current_value -= 1
    temp[current_index] = "A"
    current_index -= 1

print("".join(temp))
