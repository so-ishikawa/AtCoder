N = int(input())
pi = "3.1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679"

result = pi[:N+2]
if pi[:N+3] == "0":
    result += "0"
print(result)    