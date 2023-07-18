N, P = map(int, input().split())
a_list = list(map(int, input().split()))

print(len([x for x in a_list if x < P]))
