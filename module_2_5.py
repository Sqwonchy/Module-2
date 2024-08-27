def get_matrix(n, m, value):
    matrix = []
    for stroka in range(n):
        strok = []
        for stolbec in range(m):
            strok.append(value)
        matrix.append(strok)
        strok.clear
    print(matrix)

result1 = get_matrix(2, 2, 10)
result2 = get_matrix(3, 5, 42)
result3 = get_matrix(4, 2, 13)
