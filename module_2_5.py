# Функции в Python.Функция с параметром

def get_matrix(n, m, value):
    matrix = []
    for i in range(n):
        matrix.append([])
        for y in range(m):
            matrix[i].append(value)
    return matrix

result1 = get_matrix(2, 2, 10)
result2 = get_matrix(3, 5, 42)
result3 = get_matrix(4, 2, 13)
print(result1)
print(result2)
print(result3)


# либо можно было созджать список
#    matrix_2 = []
#    matrix.append(matrix_2)
#    for y in range(m):
#        matrix_2.append(value)
#    return matrix