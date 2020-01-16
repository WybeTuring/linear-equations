def start():
    Rows = float(input("Enter the number of rows (Of the Augmented Matrix): "))
    Columns = float(input("Enter the number of columns (Of the Augmented Matrix): "))
    print("Please enter the augmented matrix row-wise (Seperate your entries with commas)")
    Matrix = []
    for i in range(int(Rows)):
        temp = input().split(',')
        temp = [float(a) for a in temp]
        Matrix.append(temp)
    return Matrix

# The matrix must be passed in as a list of lists
def matrixPrint(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            print(round(matrix[i][j],4), end="\t")
        print()
def subMatrix(matrix):
    temp = []
    for i in range(1, len(matrix)):
        temp2 = []
        for j in range(1, len(matrix[i])):
            temp2.append(matrix[i][j])
        temp.append(temp2)
    return temp


# The matrix must be passed in as a list of lists
def pivot(matrix):
    if matrix[0][0] == 0:
        for i in range(len(matrix)):
            if matrix[i][0] != 0:
                temp = matrix[i]
                matrix[i] = matrix[0]
                matrix[0] = temp
                break
    for i in range(1, len(matrix)):
        if matrix[i][0] != 0:
            if matrix[i][0] < 0:
                factor = matrix[i][0]/matrix[0][0]
                for j in range(len(matrix[i])):
                    matrix[i][j] = matrix[i][j] - factor * matrix[0][j]
            else:
                factor = matrix[i][0] / matrix[0][0]
                for j in range(len(matrix[i])):
                    matrix[i][j] = matrix[i][j] - factor * matrix[0][j]
    return matrix

# This function eliminates the elements below the pivots from the left. Results in the reduced
# Gaussian solution of the system of linear equations.
def downwardElimination(mat1):
    temp = []
    t = len(mat1)
    for i in range(t):
        temp2 = []
        for j in range(i):
            temp2.append(0)
        if i != t - 1:
            temp3 = pivot(mat1)
            for k in range(len(temp3[0])):
                temp2.append(temp3[0][k])
            temp.append(temp2)
            mat1 = subMatrix(mat1)
        else:
            temp3 = pivot(mat1)
            for k in range(len(temp3[0])):
                temp2.append(temp3[0][k])
            temp.append(temp2)
    return temp

# This method is similar to the pivot function, but makes the entries above the pivot position zeros
def makeAboveZeros(matrix):
    temp = []
    for w in range(len(matrix) - 1, 0, -1):
        pivotPosition = 0
        t = len(matrix[0])
        # Determining the pivot on the given row
        for j in range(len(matrix[w]) - 1):
            if matrix[w][j] != 0:
                pivotPosition = j
                break

        if pivotPosition != 0 and matrix[w][pivotPosition] != 0:
            for i in range(w - 1, -1, -1):
                if matrix[i][pivotPosition] != 0:
                    factor = matrix[i][pivotPosition] / matrix[w][pivotPosition]
                    for j in range(len(matrix[i])):
                        matrix[i][j] = matrix[i][j] - factor * matrix[w][j]
        temp.append(matrix[w])
    temp.append(matrix[0])
    temp.reverse()
    return temp

# Now we need to write methods that reduce the system of linear equations to a reduced echelon form
# The function here will be quite similar to the makeAboveZeros function above, but will differ in that 
# it will always make the coefficients of the pivot one before proceeding

def reducedEchelonFormFinal(matrix):
    matrix = downwardElimination(matrix) # Obtain the echelon form matrix
    temp = []
    for w in range(len(matrix) - 1, 0, -1):
        pivotPosition = 0
        t = len(matrix[0])
        # Determining the pivot on the given row
        for j in range(len(matrix[w]) - 1):
            if matrix[w][j] != 0:
                pivotPosition = j
                break

        if pivotPosition != 0 and matrix[w][pivotPosition] != 0:
            # Make sure the pivot is one
            if matrix[w][pivotPosition] != 1:
                factor = matrix[w][pivotPosition]
                for h in range(len(matrix[w])):
                    matrix[w][h] = matrix[w][h] / factor
            for i in range(w - 1, -1, -1):
                if matrix[i][pivotPosition] != 0:
                    factor = matrix[i][pivotPosition] / matrix[w][pivotPosition]
                    for j in range(len(matrix[i])):
                        matrix[i][j] = matrix[i][j] - factor * matrix[w][j]
        temp.append(matrix[w])
    # Determining the pivot position on the first row and making sure that we convert it to one
    pivotPosition = -1
    for j in range(len(matrix[0]) - 1):
        if matrix[0][j] != 0:
            pivotPosition = j
            break
    if pivotPosition != -1 and matrix[0][pivotPosition] != 1:
        factor = matrix[0][pivotPosition]
        for h in range(len(matrix[w])):
            matrix[0][h] = matrix[0][h] / factor

    temp.append(matrix[0])
    temp.reverse()
    return temp

# Returns the reduced matrix that has the Gaussian solution to the system of linear equations
def GaussianSolution(matrix):
    return downwardElimination(matrix)

# Returns the reduced matrix that has the Row Echelon solution to the system of linear equations
def RowEchelonSolution(matrix):
    matrix = downwardElimination(matrix)
    for i in range(len(matrix)):
        pivotPosition = -1
        for j in range(len(matrix[i]) - 1):
            if matrix[i][j] != 0:
                pivotPosition = j
                break
        if pivotPosition != -1 and matrix[i][pivotPosition] != 1:
            factor = matrix[i][pivotPosition]
            for h in range(len(matrix[i])):
                matrix[i][h] = matrix[i][h] / factor
    return matrix

# Returns the reduced matrix that has the Reduced Row Echelon solution to the system of linear equations
def ReducedRowEchelonSolution(matrix):
    return reducedEchelonFormFinal(downwardElimination(matrix))

def main2():
    print("\n Now let us test with user entered data: ")
    mat = start()
    print("""   Please enter:
                    1. If you want the reduced matrix from using the Gaussian approach

                    2. If you want the reduced matrix from using the Row Echelon approach

                    3. If you want the reduced matrix from using the Reduced Row Echelon approach
        """  
    )
    x = int(input())
    while x not in [1, 2, 3]:
        print("Please enter the right choices...")
    if x in [1, 2, 3]:
        if x == 1:
            matrixPrint(GaussianSolution(mat))
        elif x == 2:
            matrixPrint(RowEchelonSolution(mat))
        else:
            matrixPrint(ReducedRowEchelonSolution(mat))
        print("\n\n\n Thanks for visiting mate!   ")
 
    
