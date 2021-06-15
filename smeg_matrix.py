# функция, которая будет создавать матрицу смежности
# from faces import faces
import numpy as np
from scipy import sparse

# функция, которая создает матрицу смежности
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


def gauss_curve_calculate(matrix_length):
    row, col = matrix_length.nonzero()
    dictinary_vertex = {}  # вспомогательный словарь, ключ -- номер вершины, значение -- список вершин, смежных с ключом
    dictinary_gauss = {}  # ключ -- вершина, значение -- пара вершин, которая с ключевой формирует грань
    for j in range(0, matrix_length.count_nonzero()):
        if row[j] not in dictinary_vertex.keys():
            dictinary_vertex[row[j]] = [col[j]]
        else:
            dictinary_vertex[row[j]].append(col[j])
    for key, val in dictinary_vertex.items():
        list_of_adjency_vertex = []
        for i in val:
            for j in val:
                if matrix_length[i, j] != 0 and matrix_length[j, i] != 0:
                    list_of_adjency_vertex.append(sorted([i, j]))
        dictinary_gauss[key] = list(map(list, {tuple(x) for x in list_of_adjency_vertex}))
    gauss_curve = np.full(len(dictinary_gauss), 2 * 3.14, )
    for key, val in dictinary_gauss.items():
        for v in val:
            a = matrix_length[v[0], v[1]]
            b = matrix_length[v[1], key]
            c = matrix_length[v[0], key]
            gauss_curve[key] -= np.arccos((b**2 + c**2 - a**2) / (2 * c * b))
    return (gauss_curve)
# def сayley_menger_determinant():
