A, B, W = map(int, input().split())
W = W * 1000

orange_count = 0
min_value = -1
max_value = -1

while True:
    orange_count += 1
    temp = W / orange_count
    if temp < A:
        break

    if A <= temp and temp <= B:
        if max_value == -1:
            max_value = orange_count
        min_value = orange_count

if min_value == -1 or max_value == -1:
    print("UNSATISFIABLE")
    exit()

print(max_value, min_value)
        
