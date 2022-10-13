N, M = map(int, input().split())
a = [list(map(int, input().split())) for l in range(N)]

max_value = 0

for first_song_number in range(M):
    for second_song_number in range(M):
        if first_song_number == second_song_number:
            continue
        temp_value = 0
        for per_score in a:
            temp_value = temp_value + max(per_score[first_song_number],per_score[second_song_number])
        
        if temp_value > max_value:
            max_value = temp_value
print(max_value)
