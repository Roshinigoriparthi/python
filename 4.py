#Yash is solving a matrix problem as part of his entrance exam preparation.
#In that matrix problem, there is a square matrix of size N x N. Yash needs to calculate the sum of the upper and lower triangular
#elements of the matrix. Help Yash solve the given matrix problem.
#Write a program that reads the NX N matrix and prints the sum of the upper and lower triangular elements.
#Note
#The upper triangle consists of elements on the anti- diagonal and above on it.
#The lower triangle consists of elements on the anti- diagonal and below it.
Code:
def calculate_triangular_sums(matrix, N):
    upper_sum = 0
    lower_sum = 0

    for i in range(N):
        for j in range(N):

            if i + j <= N - 1:
                upper_sum += matrix[i][j]
            

            if i + j >= N - 1:
                lower_sum += matrix[i][j]
    
    return upper_sum, lower_sum


N = int(input("Enter the size of the matrix (N): "))


matrix = [list(map(int, input().split())) for _ in range(N)]


upper_sum, lower_sum = calculate_triangular_sums(matrix, N)

print("Sum of upper triangular elements:", upper_sum)
print("Sum of lower triangular elements:", lower_sum)
