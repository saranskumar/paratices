import numpy as np

def input_matrix():
    """Function to take matrix input from the user element by element."""
    print("Enter matrix dimensions:")
    rows = int(input("Enter number of rows: "))
    cols = int(input("Enter number of columns: "))
    print(f"Enter the elements for a {rows}x{cols} matrix:")

    matrix = []
    for i in range(rows):
        row = []
        for j in range(cols):
            value = float(input(f"Enter element ({i + 1},{j + 1}): "))
            row.append(value)
        matrix.append(row)

    return np.array(matrix)

def matrix_sum(matA, matB):
    """Function to compute the sum of two matrices."""
    if matA.shape != matB.shape:
        raise ValueError("Matrices must have the same dimensions for addition.")
    return matA + matB

def matrix_diff(matA, matB):
    """Function to compute the difference of two matrices."""
    if matA.shape != matB.shape:
        raise ValueError("Matrices must have the same dimensions for subtraction.")
    return matA - matB

def matrix_product(matA, matB):
    """Function to compute the product of two matrices."""
    if matA.shape[1] != matB.shape[0]:
        raise ValueError("Number of columns in Matrix A must match the number of rows in Matrix B for multiplication.")
    return np.dot(matA, matB)

def display_matrix(matrix, message):
    """Function to display a matrix with a message."""
    print(message)
    for row in matrix:
        print(" ".join(map(str, row)))

# Main program
print("Enter the first matrix:")
matA = input_matrix()

print("Enter the second matrix:")
matB = input_matrix()

menu = """
MENU (Choose an option):
1. Sum of the two matrices
2. Difference of the two matrices
3. Product of the two matrices
4. Input new matrices
5. Exit
"""

while True:
    print(menu)
    choice = int(input("Enter your choice: "))

    try:
        if choice == 1:
            result = matrix_sum(matA, matB)
            display_matrix(result, "Sum of the matrices:")
        elif choice == 2:
            result = matrix_diff(matA, matB)
            display_matrix(result, "Difference of the matrices:")
        elif choice == 3:
            result = matrix_product(matA, matB)
            display_matrix(result, "Product of the matrices:")
        elif choice == 4:
            print("Re-enter the matrices:")
            matA = input_matrix()
            matB = input_matrix()
        elif choice == 5:
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")
    except ValueError as e:
        print(f"Error: {e}")
