class Solution(object):
    def setZeroes(self, matrix):
        m =len(matrix)
        n = len(matrix[0])
        
        row = [0] *m
        col = [0] *n

        for i in range(0,m):
            for j in range(0,n):
                if(matrix[i][j] == 0):
                    col[j] = 1
                    row[i] = 1
        for i in range(0,m):
            for j in range(0,n):
                if(col[j] == 1 or row[i] == 1):
                    matrix[i][j] = 0
        return matrix