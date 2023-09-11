class Solution(object):
    def searchMatrix(self, matrix, target):
        f = 0
        for i in range(len(matrix)):
            if target in matrix[i]:
                return True
        return False