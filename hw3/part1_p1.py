import numpy as np
c = 0.1
learn = 0.2
b = -2
w = np.array([0,1,b])*c
x = np.array([[1,4,1],[2,2,1],[3,4,1],[1,1,1],[2,1,1],[3,1,1]])
y = np.array([1,1,1,-1,-1,-1])
missed = np.zeros(6)

for i in range(len(x)):
    miss = w.dot(x[i])
    if(miss>=1):
        missed[i] = 1
    elif(miss<= -1):
        missed[i] = -1
    else:
        missed[i] = 0 

for j in range(x.shape[1]):
    for i in range(len(x)):
        if(y[i]!=missed[i]):
            penalty = (-y[i]*x[i][j])
        w[j]=w[j] - (learn * (w[j] + c * penalty))



