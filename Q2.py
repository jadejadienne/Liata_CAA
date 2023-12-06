def matrix_multiply_recursive(A, B):
    n = len(A)

    if not (len(A) == len(A[0]) == len(B) == len(B[0]) == n):
        raise ValueError("As matrizes não são quadradas ou têm tamanhos diferentes")


    if n == 1:
        return [[A[0][0] * B[0][0]]]

  
    mid = n // 2
    A11 = [row[:mid] for row in A[:mid]]
    A12 = [row[mid:] for row in A[:mid]]
    A21 = [row[:mid] for row in A[mid:]]
    A22 = [row[mid:] for row in A[mid:]]

    B11 = [row[:mid] for row in B[:mid]]
    B12 = [row[mid:] for row in B[:mid]]
    B21 = [row[:mid] for row in B[mid:]]
    B22 = [row[mid:] for row in B[mid:]]

   
    P1 = matrix_multiply_recursive(A11, B11)
    P2 = matrix_multiply_recursive(A12, B21)
    P3 = matrix_multiply_recursive(A11, B12)
    P4 = matrix_multiply_recursive(A12, B22)
    P5 = matrix_multiply_recursive(A21, B11)
    P6 = matrix_multiply_recursive(A22, B21)
    P7 = matrix_multiply_recursive(A21, B12)
    P8 = matrix_multiply_recursive(A22, B22)

  
    result = [[0] * n for _ in range(n)]

    for i in range(mid):
        for j in range(mid):
            result[i][j] = P1[i][j] + P2[i][j]
            result[i][j + mid] = P3[i][j] + P4[i][j]
            result[i + mid][j] = P5[i][j] + P6[i][j]
            result[i + mid][j + mid] = P7[i][j] + P8[i][j]

    return result

A = [[1, 2, 3, 4],
     [5, 6, 7, 8],
     [9, 10, 11, 12],
     [13, 14, 15, 16]]

B = [[17, 18, 19, 20],
     [21, 22, 23, 24],
     [25, 26, 27, 28],
     [29, 30, 31, 32]]

result = matrix_multiply_recursive(A, B)

for row in result:
    print(row)
