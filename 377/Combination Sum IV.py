class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        
        if not nums or target == 0:
            return 0
        
        nums.sort()
        dp = (target+1)*[0]
        
        for item in nums:
            if item <= target:
                dp[item] = 1
        
        for i in range(target+1):
            for item in nums:
                if i - item >= 0:
                    dp[i] += dp[i-item]
                else:
                    break
                    
        return dp[-1]
        