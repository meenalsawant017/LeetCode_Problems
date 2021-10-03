matrix = [
    [1,2,2,3],
    [3,4,10,4],
    [2,10,1,2],
    [5,4,4,5],
]

size = 2 # 2 x 2

def get_beauty(sub_matrix):
    sm = sorted(sub_matrix)
    magic_num = 1
    for num in sm:
        if num > magic_num:
            return magic_num
        magic_num += 1
    return magic_num

def magic_number(matrix):
    sub_matrices = []
    serial = 0
    for j in range(size):
        for i in range(size):
            x, y = j * len(matrix)//size, i * len(matrix)//size

            sub_matrix = []
            for p in range(size):
                for q in range(size):
                    sub_matrix.append(matrix[x+p][y+q])

            beauty_num = get_beauty(sub_matrix)
            sub_matrices.append([sub_matrix, beauty_num, serial])
            serial += 1

    sub_matrices.sort(key=lambda x: (x[1],x[2]))

    serial = 0
    for j in range(size):
        for i in range(size):
            x, y = j * len(matrix)//size, i * len(matrix)//size

            iter1 = iter(sub_matrices[serial][0])
            for p in range(size):
                for q in range(size):
                    matrix[x+p][y+q] = next(iter1)
            serial += 1

    for row in matrix:
        print(row)

    return matrix

magic_number(matrix)
