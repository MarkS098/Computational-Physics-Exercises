from numpy.linalg import solve

A = ([1,1,-1],
     [-1,0,-1],
     [0,-20,-1])

v = (0 , 8, -12)

x = solve(A,v)
