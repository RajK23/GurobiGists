from gurobipy import *


'''
Simple MIP Formulation to solve Sudoku

Sets:
I : rows
J : columns:
K : numbers {1, 2, 3, 4, 5, 6, 7, 8, 9}


Data:
Presolved_ij 



'''

#Sets

I = range(9)
J = range(9)
K = range(9)

m = Model();

X = {(i,j,k) : m.addVar(vtype = GRB.BINARY) for i in I for j in J for k in K}


for i in I:
    for j in J:
        m.addConstr(quicksum(X[i, j, k] for k in K) == 1)

for i in I:
    for k in K:
        m.addConstr(quicksum(X[i, j, k] for j in J) == 1)

for j in I:
    for k in K:
        m.addConstr(quicksum(X[i, j, k] for i in I) == 1)


for ii in range(3):
    for jj in range(3):
        for k in K:
            m.addConstr(quicksum(X[i,j,k] for i in range(3*ii,3*ii+3) for j in range(3*jj,3*jj+3))==1)

for k in K:
    m.addConstr(quicksum(X[x,x,k] for x in range(9)) == 1)

m.optimize();

for i in I:
    a = ""
    for j in J:
        for k in K:
            if (X[i, j, k].x > 0.9) :
                a += str(k + 1)
        if ((j+1) % 3 == 0) :
            a += "|"
    print(a)
    if ((i + 1) % 3 == 0) :
        print("------------")


