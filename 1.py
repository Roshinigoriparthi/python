#Write a program that reads an M x N matrix and prints the perimeter of the matrix.
#Note
#The perimeter of the matrix is defined as the sum of all the elements on the four edges of the matrix.
#Input
#The first line of input contains space-separated integers representing M and N respectively.
#The next M lines of input contain N space-separated integers representing the matrix.
code:
# Function to calculate the perimeter of the matrix
def calculate_perimeter(matrix, M, N):
    perimeter_sum = 0
    perimeter_sum += sum(matrix[0])       
    perimeter_sum += sum(matrix[M-1])     
    
    for i in range(1, M-1):
        perimeter_sum += matrix[i][0]    
        perimeter_sum += matrix[i][N-1]   
    
    return perimeter_sum

M, N = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(M)]


perimeter = calculate_perimeter(matrix, M, N)
print(perimeter)
