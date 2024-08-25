my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
while len(my_list) > 0 or s > 0:
    s = my_list.pop(0)
    if s >= 0:
        if s > 0:
            print(s)
    else:
        break

