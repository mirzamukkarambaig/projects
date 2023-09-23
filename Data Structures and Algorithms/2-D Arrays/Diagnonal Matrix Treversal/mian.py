def diagonal_traversal(matrix):
    num_rows = len(matrix)
    num_columns = len(matrix[0]) if matrix else 0

    for i in range(num_rows + num_columns - 1):
        print('Diagonal ', i + 1, ': ', end = '')
        
        # Determine the starting row and column for the current diagonal
        start_row = min(i, num_rows - 1)
        start_col = i - start_row
        
        row, col = start_row, start_col
        while row >= 0 and col < num_columns:
            print(matrix[row][col], end=' ')
            row -= 1
            col += 1
        
        print()

matrix = [ [1 , 2 , 3, 4],
           [5 , 6 , 7, 8],
           [9 , 10, 11, 12],
]

# Call the function with the corrected traversal
diagonal_traversal(matrix)
