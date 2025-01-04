L, R = map(int, input().split())

first_digit = 0
while L > 10**first_digit:
    first_digit += 1
print(first_digit)
end_digit = 0
