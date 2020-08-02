class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        
        if not nums:
            return None
        
        s = set()
        s.add(nums[0])
        
        for i in range(1,len(nums)):
            if len(s) < 3:
                s.add(nums[i])
            elif nums[i] not in s and nums[i] > min(s):
                s.add(nums[i])
                s.remove(min(s))
        
        if len(s) < 3:
            return max(s)
        else:
            return min(s)
            