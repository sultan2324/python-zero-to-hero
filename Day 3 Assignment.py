dic = {"a":1, "b":2, "c":5, "d":4}

dic_max = max(dic, key=dic.get)
print("Maximum value in dictionary is : ", dic_max, "-->", dic[dic_max])
