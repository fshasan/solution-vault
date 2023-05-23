class Solution(object):
    def searchMatrix(self, matrix, target):
        f = 0
        for i in range(len(matrix)):
            if target in matrix[i]:
                f = 1
                break
        if f == 1:
            return True
        else:
            return False