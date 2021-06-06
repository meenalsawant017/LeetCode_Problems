"""
Rotate matrix around diagonals.
Given an n x n matrix M, where n is odd and n > 1, and an integer k,
rotate M counterclockwise k times which are not on the main diagonal or
on the diagonal from the top right to the bottom left.
Return the new matrix.
Ex. I put *s to show which elements are fixed on the diagonals.

[*1*, 2, 3, 4, *5*]
[6, *7*, 8, *9*, 10]
[11, 12, *13*, 14, 15]
[16, *17*, 18, *19*, 20]
[*21*, 22, 23, 24, *25*]

Rotates to:

[*1*, 16, 11, 6, *5*]
[22, *7*, 12, *9*, 2]
[23, 18, *13*, 8, 3]
[24, *17*, 14, *19*, 4]
[*21*, 20, 15, 10, *25*]
"""


matrix = [
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15],
    [16, 17, 18, 19, 20],
    [21, 22, 23, 24, 25],
]

def reverseImage(matrix):
    start, end = 0, len(matrix)-1

    while start < end:
        for i in range(len(matrix)):
            if start != i and end!= i:
                matrix[start][i], matrix[end][i] = matrix[end][i], matrix[start][i]
        start += 1
        end -= 1
    return matrix

def swapMatrix(matrix):
    for i in range(len(matrix)):
        for j in range(i+1, len(matrix)):
            if i != j and i+j != len(matrix) -1:
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    return matrix


def rotateImage(matrix, num_rotate):
    num_rotate = num_rotate % 4 # because 4 rotations = original image

    for _ in range(num_rotate):
        matrix = reverseImage(matrix)
        matrix = swapMatrix(matrix)

    return matrix

print(rotateImage(matrix, 17))
