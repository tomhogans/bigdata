import numpy as np

matrix = np.array([[1, 1, 1],
                  [1, 2, 3],
                  [1, 3, 5]])

# Get eigenvalues and eigenvectors
w, v = np.linalg.eig(matrix)
print("Matrix:")
print(matrix)
print("Eigenvalues: %s" % w)
print("Eigenvectors: %s" % v)

# Implement matrix powers method and compare results
matrix = np.linalg.matrix_power(matrix, 2)
print("Powered Matrix:")
print(matrix)
print("Eigenvalues: %s" % w)
print("Eigenvectors: %s" % v)
