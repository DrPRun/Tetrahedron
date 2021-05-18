# функция, которая будет создавать матрицу смежности
# from faces import faces
import numpy as np
from scipy import sparse


def adjacency_matrix(faces, vertex):
    row = []
    col = []
    for fs in faces:
        row.append(fs[0])
        col.append(fs[1])
        row.append(fs[0])
        col.append(fs[2])
        row.append(fs[1])
        col.append(fs[2])
        col.append(fs[0])
        row.append(fs[1])
        col.append(fs[0])
        row.append(fs[2])
        col.append(fs[1])
        row.append(fs[2])
    data = [1.] * len(row)  # массив единиц, нужен для конструктора разреженной матрицы
    space_row = np.array(row)
    space_col = np.array(col)
    space_data = np.array(data)
    adj_max = sparse.coo_matrix((space_data, (space_row, space_col)), shape=(vertex, vertex)).tocsc()
    return adj_max

def gauss_curve_calculate(matrix_length, vertex):
    initial_curve = np.full(vertex, 2*3.14) # создаем массив данных с одинаковыми значениями
    # for i in range(0, vertex):
    #     initial_curve[i] = 2*3.14
    for j in range(0, matrix_length.count_nonzero()):
        row, col = matrix_length.nonzero()

        print(row[j], col[j], matrix_length[row[j], col[j]])
    # print(initial_curve)

