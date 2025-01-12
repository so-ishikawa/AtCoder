Dig, Dis = map(int, input().split())

def my_round(number, ndigits=0):
    p = 10**ndigits
    return (number * p * 2 + 1) // 2 / p
# print(my_round(0.25, 1))
# exit()


dir_list = ["N", "NNE", "NE", "ENE", "E", "ESE", "SE", "SSE", "S", "SSW",
            "SW", "WSW", "W", "WNW", "NW", "NNW"]
Dig /= 10
# Dis = round(Dis/60, 1)
Dis = my_round(Dis/60, 1)

if 0.0 <= Dis <= 0.2:
    print("C", end=" ")
elif Dig < 11.25 or 348.75 < Dig:
    print(dir_list[0], end=" ")
else:
    for i in range(1, len(dir_list)):
        if 11.25 + (i-1)*(360/16) <= Dig < 11.25 + i*(360/16):
            print(dir_list[i], end=" ")



if 0.0 <= Dis <= 0.2:
    print(0)
elif 0.3 <= Dis <= 1.5:
    print(1)
elif 1.6 <= Dis <= 3.3:
    print(2)
elif 3.4 <= Dis <= 5.4:
    print(3)
elif 5.5 <= Dis <= 7.9:
    print(4)
elif 8.0 <= Dis <= 10.7:
    print(5)
elif 10.8 <= Dis <= 13.8:
    print(6)
elif 13.9 <= Dis <= 17.1:
    print(7)
elif 17.2 <= Dis <= 20.7:
    print(8)
elif 20.8 <= Dis <= 24.4:
    print(9)
elif 24.5 <= Dis <= 28.4:
    print(10)
elif 28.5 <= Dis <= 32.6:
    print(11)
else:
    print(12)
