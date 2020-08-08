from gurobipy import *


'''
Formulation:
Simple MIP Formulation to Solve Diagonal Sudoku

Sets:
I : rows
J : columns:
K : numbers {1, 2, 3, 4, 5, 6, 7, 8, 9}


Data:
pre_ij : Preassigned Squares




'''

#Sets

# Pre = [ 
#         [6,4,0, 0,0,7, 0,2,0], 
#         [0,0,2, 0,4,0, 0,0,0], 
#         [3,0,0, 9,6,2, 0,0,0],

#         [5,0,0, 0,0,0, 0,0,0], 
#         [4,9,0, 0,0,0, 0,7,2], 
#         [0,0,0, 0,0,0, 0,0,5],

#         [0,0,0, 7,2,3, 0,0,6], 
#         [0,0,0, 0,9,0, 2,0,0], 
#         [0,3,0, 1,0,0, 0,4,9]
#     ]

Pre = [ 
        [0,4,0, 8,0,0, 0,6,0], 
        [0,0,0, 0,0,0, 9,3,0], 
        [0,0,0, 6,0,3, 0,0,2],

        [2,0,0, 4,0,7, 8,0,0], 
        [3,0,0, 0,0,0, 0,0,0], 
        [0,0,0, 0,0,0, 0,0,5],

        [0,0,0, 0,0,0, 0,0,9], 
        [8,9,0, 0,1,0, 0,2,0], 
        [6,0,5, 0,2,0, 0,0,0]
    ]
I = range(9)
J = range(9)
K = range(9)

m = Model();

X = {(i,j,k) : m.addVar(vtype = GRB.BINARY) for i in I for j in J for k in K}

for i in range(9):
    for j in range(9):
        if (Pre[i][j] != 0): 
            m.addConstr(X[i, j, Pre[i][j]-1] == 1)


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
            m.addConstr(quicksum(X[i,j,k] for i in range(3 * ii,3 * ii+3) for j in range(3 * jj,3 * jj + 3)) == 1)

for k in K:
    m.addConstr(quicksum(X[n,n,k] for n in range(9)) == 1)

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


