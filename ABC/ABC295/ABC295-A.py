N = int(input())
w_list = input().split() #list(map(int, input().split()))

if "and" in w_list:
    print("Yes")
elif "not" in w_list:
    print("Yes")
elif "that" in w_list:
    print("Yes")
elif "the" in w_list:
    print("Yes")
elif "you" in w_list:
    print("Yes")
else:
    print("No")
