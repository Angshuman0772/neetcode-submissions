class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        row = len(matrix)
        col = len(matrix[0])

        top = 0
        bottom = row - 1

        while top <= bottom:
            selectedRow = (top + bottom) // 2

            if target > matrix[selectedRow][-1]:
                top = selectedRow + 1
            
            elif target < matrix[selectedRow][0]:
                bottom = selectedRow - 1
            
            else:
                break
        
        if not (top <= bottom):
            return False
        
        l = 0
        r = col - 1
        row = (top + bottom) // 2

        while l <= r:
            mid = (l + r) // 2

            if target > matrix[row][mid]:
                l = mid + 1
            
            elif target < matrix[row][mid]:
                r = mid - 1
                
            else:
                return True
        return False
