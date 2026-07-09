class Solution(object):
    def rotate(self, matrix):
     n =len(matrix)
     arr = [[0] * n for _ in range(n)]
     z = n-1
     for i in range(0,n):
        
        for j in range(0,n):
          arr[j][z] = matrix[i][j]
        z = z - 1
     for i in range(n):
        for j in range(n):
          matrix[i][j] = arr[i][j]
     return matrix