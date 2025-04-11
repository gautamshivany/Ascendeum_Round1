import numpy as np

def generate_spiral_matrix(n):
    matrix = [[0]*n for _ in range(n)]
    top , bottom = 0, n-1
    left, right = 0, n-1
    num = 1 
    
    while num <= n * n:
        for i in range(left, right + 1):
            matrix[top][i] = num
            num += 1
        top += 1
        
        for i in range(top, bottom + 1):
            matrix[i][right] = num ###
            num += 1
        right -= 1
        
        for i in range(right, left-1, -1):
            matrix[bottom][i] = num
            num += 1
        bottom -= 1
        
        for i in range(bottom, top-1,-1):
            matrix[i][left] = num
            num += 1
        left += 1
        
    return matrix
    
n = 6
result = generate_spiral_matrix(6)

#for row in result:
#    print(row)

for row in result:
    for x in row:
        print(x , end=" " )
    print("")


#To print in a 2D Array
#print(generate_spiral_matrix(4))
