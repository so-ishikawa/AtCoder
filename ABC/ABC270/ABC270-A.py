A, B = map(int, input().split())
result_score = 0

if A == 1 or A == 3 or A == 5 or A == 7 or B == 1 or B == 3 or B == 5 or B == 7:
    result_score += 1

if A == 2 or A == 3 or A == 6 or A == 7 or B == 2 or B == 3 or B == 6 or B == 7:
    result_score += 2

if A == 4 or A == 5 or A == 6 or A == 7 or B == 4 or B == 5 or B == 6 or B == 7:
    result_score += 4

print(result_score)
