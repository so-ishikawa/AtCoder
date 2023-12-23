S = input()

min_value = 99999999999999
for i in range(len(S)-2):
    temp = int(S[i:i+3])
    result = abs(753-temp)
    if result < min_value:
        min_value = result
print(min_value)
