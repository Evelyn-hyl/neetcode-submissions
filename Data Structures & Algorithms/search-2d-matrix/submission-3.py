class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        i = 0
        rows = len(matrix)
        columns = len(matrix[0])
        l, r = 0, columns - 1

        while target > matrix[i][r]:
            i += 1
            if i > rows - 1:
                return False
        
        while l <= r:
            mid = l + (r - l) // 2

            if target == matrix[i][mid]:
                return True
            
            if target > matrix[i][mid]:
                l = mid + 1
            else:
                r = mid - 1
        
        return False



        