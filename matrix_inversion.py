def determinant(matrix):
    n = len(matrix)
    if n == 1:
        return matrix[0][0]
    if n == 2:
        return matrix[0][0]*matrix[1][1] - matrix[0][1]*matrix[1][0]
    det = 0
    for col in range(n):
        sign = (-1) ** col
        submatrix = [row[:col] + row[col+1:] for row in matrix[1:]]
        det += sign * matrix[0][col] * determinant(submatrix)
    return det

def matrix_inverse(A):
    n = len(A)
    for row in A:
        if len(row) != n:
            raise ValueError("Matrix must be square.")
    det = determinant(A)
    if det == 0:
        raise ValueError("Matrix is singular and cannot be inverted.")
    adj = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            minor = [row[:j] + row[j+1:] for row in A[:i] + A[i+1:]]
            sign = (-1) ** (i + j)
            adj[j][i] = sign * determinant(minor)
    inverse = [[adj[i][j]/det for j in range(n)] for i in range(n)]
    return inverse