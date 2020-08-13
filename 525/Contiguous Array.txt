class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        dic = {}
        dic[0] = [-1]
        
        nums = [-1 if item == 0 else 1 for item in nums]
        
        cnt = 0
        for i, item in enumerate(nums):
            cnt += item
            
            if cnt in dic:
                dic[cnt].append(i)
            else:
                dic[cnt] = [i]
        

        max_len = 0
        for item in dic.values():
            max_len = max(max_len,(item[-1] - item[0]))
            
        return max_len