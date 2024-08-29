
a: int = int(input("Введите целое число от 3 до 20: "))
list_ = []
for one_num in range(1, a):
    two_num = a - 1
    while one_num != two_num:
        if a % (one_num + two_num) == 0:
            list_.append(one_num)
            list_.append(two_num)
        two_num -= 1


print(*list_)











# по другом хотел пойти.
# a: int = 20
# list_ = []
# for all_numb in range(1, a):
#     number = all_numb + 1
#     for numb in range(number,a):
#         if number == 1:
#             continue
#         elif a % (all_numb + numb):
#             list_.append(all_numb)
#             list_.append(numb)
#         else:
#             continue
#
# print(*list_, sep=" ")
