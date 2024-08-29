
# a: int = int(input("Введите целое число от 3 до 20: "))
# list_ = []
# for one_num in range(1, a):
#     two_num = a - 1
#     while one_num != two_num:
#         if a % (one_num + two_num) == 0:
#             list_.append(one_num)
#             list_.append(two_num)
#         two_num -= 1
#
#
# print(*list_)

# ВСЕ я исправил чтобы порядок цифр был как у вас

a: int = int(input("Введите целое число от 3 до 20: "))
list_ = []
for one_num in range(1, a):
    two_num = one_num + 1
    while two_num != a:
        if a % (one_num + two_num) == 0:
            list_.append(one_num)
            list_.append(two_num)
        two_num += 1
print(*list_)








