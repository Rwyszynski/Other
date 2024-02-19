def main_diagonal_product(mat):
    height = len(mat[0])
    lis = 1
    for i in range(height):
        let = mat[i][i]
        lis = let * lis


    
    return lis

print(main_diagonal_product([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
