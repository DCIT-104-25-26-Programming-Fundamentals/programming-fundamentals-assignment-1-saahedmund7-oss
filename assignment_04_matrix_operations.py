# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 4
# Topic: Multi-dimensional Arrays (2D Lists), Nested Loops, and Functions
# =============================================================================
#
# TASK: Matrix Operations
#
# Write a Python program that performs three operations on matrices (2D lists),
# each implemented in its own function.
#
# -----------------------------------------------------------------------------
# PART A — Transpose a Matrix
# -----------------------------------------------------------------------------
# - Read an M x N matrix from the user.
# - Compute and display its transpose (rows become columns, columns become rows).
#
# Example (2 x 3 input):
#
#   Original Matrix:      Transposed Matrix:
#   1  2  3               1  4
#   4  5  6               2  5
#                         3  6
#
# -----------------------------------------------------------------------------
# PART B — Add Two Matrices
# -----------------------------------------------------------------------------
# - Read two matrices of exactly the same size (M x N).
# - Compute their element-wise sum and display the result.
#   (Each position in the result = the sum of the values at that position
#    in both matrices.)
#
# -----------------------------------------------------------------------------
# PART C — Multiply Two Matrices
# -----------------------------------------------------------------------------
# - Read matrix A of size M x N and matrix B of size N x P.
#   (The number of COLUMNS in A must equal the number of ROWS in B.)
# - Compute and display the matrix product A × B (result is M x P).
#
# -----------------------------------------------------------------------------
# EXPECTED INPUT FORMAT
# -----------------------------------------------------------------------------
# When entering a row, the user types all values on one line separated by spaces:
#
#   Enter number of rows: 2
#   Enter number of columns: 3
#   Enter row 1: 1 2 3
#   Enter row 2: 4 5 6
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - Use nested loops for all operations (no NumPy or other libraries).
# - Each operation must be in its own function (see scaffold below).
# - Display each matrix in a neat, aligned grid format.
# - Tip: Complete Part A first, then Parts B and C.
#

#
# =============================================================================
# YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in
# =============================================================================

# Topic: Multi-dimensional Arrays (2D Lists), Nested Loops, and Functions

def get_matrix():
    rows=int(input("Enter number of rows: "))
    cols=int(input("Enter number of columns: "))
    matrix=[]
    print("Enter the matrix row by row:")
    for i in range(rows):
        row=[]
        for j in range(cols):
            val=int(input(f"Enter value for row {i+1}, column {j+1}: "))
            row.append(val)
    matrix.append(row)
    return matrix

Part A — Transpose a Matrix
def transpose_matrix():
    print("--- Transpose Matrix ---")
    matrix=get_matrix()

    rows=len(matrix)
    cols=len(matrix[0])

    # Create a new matrix for the transpose
    transpose=[]
    for j in range(cols):
        new_row=[]
        for i in range(rows):
            new_row.append(matrix[i][j])
        transposed.append(new_row)

        print("/nOriginal Matrix:")
        for row in matrix:
            print(row)

    print("\nTransposed Matrix:")
    for row in transposed:
        print(row)

#Part B — Add Two Matrices
def add_matrices(): 
    print("--- Add Two Matrices ---")
    print("Enter first matrix:")
    mat1=get_matrix()

    print("Enter second matrix:") 
    mat2=get_get_matrix_matching(len(mat1), len(mat1[0])) if 'get_get_matrix_matching ' else get_matrix()

    rows=len(mat1)
    cols=len(mat1[0])   

    result=[]
    for i in range(rows):
        new_row=[]
        for j in range(cols):
            new_row.append(mat1[i][j]+mat2[i][j])
        result.append(new_row)        

    print("\nResultant Matrix:")
    for row in result:
        print(row)

        if _name_=="_main_":
            #Run the functions to demonstrate their functionality
            transpose_matrix()
            