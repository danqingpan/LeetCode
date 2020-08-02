class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        
        s = sum(nums)
        if s%2 == 1:
            return False
        
        target = s//2
        
        dp = (target+1)*[False]
        dp[0] = True
        
        for item in nums:
            for i in reversed(range(item,target+1)):
                dp[i] = dp[i] | dp[i-item]
                
        return dp[-1]
