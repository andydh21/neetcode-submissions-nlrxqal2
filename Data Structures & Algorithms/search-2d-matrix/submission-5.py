class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for subArray in matrix:
            left = 0 
            right = len(subArray) - 1
            
            while left <= right:
                mid = (left + right)//2

                if subArray[mid] < target:
                    left = mid + 1
                elif subArray[mid] > target:
                    right = mid - 1
                else:
                    return True
        
        return False