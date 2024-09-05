#Write a program that reads an Nx N matrix and checks if it is a unique matrix or not.
#4
#5
#6-
#Note
#7
#8-
#A Unique Matrix is a matrix in which every row and column contains all integers from 1 to N.
#9
#10-
#11
#12
#13 n-
#Input
#The first line of input contains an integer representing N.
#14 che
#15 mai
#The next N lines of input contain N space-separated integers representing the matrix.
#16 tra
#17

code:

def is_unique_matrix(matrix, N)
    unique_set = set(range(1, N + 1))

    for row in matrix:
        if set(row) != unique_set:
            return False
    
    for col in range(N):
        col_elements = {matrix[row][col] for row in range(N)}
        if col_elements != unique_set:
            return False

    return True

N = int(input("Enter the size of the matrix (N): "))
matrix = [list(map(int, input().split())) for _ in range(N)]

if is_unique_matrix(matrix, N):
    print("Yes, the matrix is a unique matrix.")
else:
    print("No, the matrix is not a unique matrix.")

