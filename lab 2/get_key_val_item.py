def get_values(dic):

    print("keys in dictionary")
    for key in dic.keys():
        print(key)
    print("values in dictionary")
    for value in dic.values():
        print(value)
    print("items in dictionary")
    for item in dic.items():
        print(item)

dict_num = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
get_values(dict_num)