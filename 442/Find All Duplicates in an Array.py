class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        s = set(nums)
        for i in range(len(nums)):
            nums[abs(nums[i])-1] = -nums[abs(nums[i])-1]
        
        result = []
        for i in range(len(nums)):
            if nums[i] > 0 and i+1 in s:
                result.append(i+1)
                
        return result