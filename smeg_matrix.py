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
    row , col = matrix_length.nonzero()
    dictinary_vertex = {}
    dictinary_gauss = {}
    for j in range(0, matrix_length.count_nonzero()):
        if row[j] not in dictinary_vertex.keys():
            dictinary_vertex[row[j]] = [col[j]]
        else:
            dictinary_vertex[row[j]].append(col[j])
    for key, val in dictinary_vertex.items():
        list_of_adjency_vertex = []
        for i in val:
            for j in val:
                if (matrix_length[i,j] != 0 and matrix_length[j,i] != 0):
                    list_of_adjency_vertex.append(sorted([i,j]))
        dictinary_gauss[key] = list(map(list, { tuple(x) for x in list_of_adjency_vertex } ))
        # print(list_of_adjency_vertex)
    print(dictinary_gauss)
