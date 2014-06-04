import numpy as np
from scipy import linalg as LA
from scipy.linalg import svd

M = np.array([[1, 2, 3], [3, 4, 5], [5, 4, 3], [0, 2, 4], [1, 3, 5]])

Mt = M.transpose()

#Mt dot M
u = np.dot(Mt, M)
print "\nMtranspose dot M"
print u

#M dot Mt
v = np.dot(M, Mt)
print "\nM dot Mtranspose"
print v

#Eig values and vecs
e_vals, e_vacs = LA.eig(u)
e_vals1, e_vacs1 = LA.eig(v)

print "\nEigen values"
print e_vals, e_vals1

print "\n\nEigen vectors"
print e_vacs, e_vacs1

#SVD
U, s, V = LA.svd(M)
print "U:"
print U

print "V:"
print V

print "Sigma:"
print s
dim = 1
rows, cols = M.shape

for index in xrange(dim, rows):
   # s[index] = 0

    reM= np.dot(np.dot(U,LA.diagsvd(s,len(M),len(V))),V)
print "SVD:"
print reM


#set s[1], s[2] = 0

s[1] = 0
s[2] = 0
print "reduced sigma:"
print s

for index in xrange(dim, rows):
    # s[index] = 0
    
    reM= np.dot(np.dot(U,LA.diagsvd(s,len(M),len(V))),V)



