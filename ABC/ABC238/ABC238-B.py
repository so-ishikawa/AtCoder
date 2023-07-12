N = int(input())
A_list = list(map(int, input().split()))

actual_pizza_degree_list = [0]*N
pre_degree = 0
for i in range(len(A_list)):
    temp =  (pre_degree + A_list[i]) % 360
    actual_pizza_degree_list[i] = temp
    pre_degree = temp

# print(actual_pizza_degree_list)

if 360 not in actual_pizza_degree_list:
    actual_pizza_degree_list.append(360)
if 0 not in actual_pizza_degree_list:
    actual_pizza_degree_list.append(0)

actual_pizza_degree_list.sort()
# print(actual_pizza_degree_list)
degree_list = [0]*(len(actual_pizza_degree_list)-1)
for i in range(1, len(actual_pizza_degree_list)):
    degree_list[i-1] = actual_pizza_degree_list[i] - actual_pizza_degree_list[i-1]
# print(degree_list)
print(max(degree_list))
