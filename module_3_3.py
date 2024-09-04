print()  #1) для разделения между заданиями

def print_params(a=1, b='строка', c=True):
    print(a, b, c)
print_params()
print_params(b=25)
print_params(c=[1, 2, 3])
print_params(c=1, b=2, a=3)

print()  #2) для разделения между заданиями

values_list = ["a", 10, True]
values_dict = {"a": "B", "b": 5, "c": False}
print_params(*values_list)
print_params(**values_dict)

print()  #3) для разделения между заданиями

values_list_2 = ["Первый обьект", False]
print_params(*values_list_2, 42)
print_params(28, *values_list_2)