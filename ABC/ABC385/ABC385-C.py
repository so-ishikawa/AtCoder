N = int(input())
H_list = list(map(int, input().split()))

max_length = 1
for time in range(1, 3000+1):
    for start in range(time):
        last = None
        length = 0
        count = 0
        while True:
            if start + time*count >= len(H_list):
                break
            temp = H_list[start+time*count]
            if last == temp:
                length += 1
                if max_length < length:
                    max_length = length
            else:
                last = temp
                length = 1
            count += 1
print(max_length)
