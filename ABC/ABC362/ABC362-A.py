R, G, B = map(int, input().split())
C = input()

dic_ = dict({"Red":R, "Green":G, "Blue":B})
#delete_item = dic_[C]
dic_.pop(C)
print(min(dic_.values()))
