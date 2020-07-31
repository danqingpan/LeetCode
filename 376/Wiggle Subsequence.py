class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:

        if not nums:
            return 0
        
        l = len(nums)
        
        dp_s = l*[0]; dp_s[0] = 1
        dp_l = dp_s.copy()

        for i in range(1,l):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp_l[i] = max(dp_l[i], dp_s[j]+1)

                elif nums[i] < nums[j]:
                    dp_s[i] = max(dp_s[i], dp_l[j]+1)
        
        return max(max(dp_l),max(dp_s))
        