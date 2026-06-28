class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) == 0:
            return -1

        start = 0
        end = len(nums) - 1

        while (start <= end):
            mid = (start + end)//2

            if (nums[mid] < target):
                start = mid + 1
                continue
            
            elif (nums[mid] > target):
                end = mid - 1
                continue
            
            else:
                return mid
        
        return -1