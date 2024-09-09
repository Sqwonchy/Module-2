def calculate_structure_sum(*data):
    data_ = data[0]
    all = 0
    if len(data_) == 0:
        return 0
    value_=data_[0]
    str_ = isinstance(value_, str)
    int_ = isinstance(value_, int)
    list_ = isinstance(value_, list)
    tuple_ = isinstance(value_, tuple)
    dict_ = isinstance(value_,dict)
    set_ = isinstance(value_, set)
    if str_ == True:
        if len(data_) == 1:
            return all + len(value_)
        else:
            all += len(value_) + calculate_structure_sum(data_[1:])
    elif int_ == True:
        if len(data_) == 1:
            return all + value_
        else:
            all += (value_ +calculate_structure_sum(data_[1:]))
    elif list_ == True:
        if len(value_)>0:
            if len(data_) == 1:
                return all + ((calculate_structure_sum(value_)))
            else:
                all += ((calculate_structure_sum(value_) + calculate_structure_sum(data_[1:])))
        else:
            return 0
    elif dict_ == True:
        dict_numb = []
        for key , val in value_.items():
            dict_numb.append(key)
            dict_numb.append(val)
        all += (calculate_structure_sum(dict_numb) + calculate_structure_sum(data_[1:]))
    elif tuple_ == True:
        if len(data_) == 1:
            return all + (calculate_structure_sum(list(value_)))
        else:
            all += (calculate_structure_sum(list(value_))+ calculate_structure_sum(data_[1:]))
    elif set_ == True:
        if len(data_)== 1:
            set_list = []
            for k in value_:
                set_list.append(k)
            return all + (calculate_structure_sum(set_list))
        else:
            set_list = []
            for k in value_:
                set_list.append(k)
            all += (calculate_structure_sum(set_list)) + calculate_structure_sum(data_[1:])
    return all

data_structure = [
[1, 2, 3],
{'a': 4, 'b': 5},
(6, {'cube': 7, 'drum': 8}),
"Hello",
((), [{(2, 'Urban', ('Urban2', 35))}])
]

result = calculate_structure_sum(data_structure)
print(result)

