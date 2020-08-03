class Solution:
    def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
        
        dic = {}
        count = 0
        for c in C:
            for d in D:
                x = c+d
                if x in dic:
                    dic[x] += 1
                else:
                    dic[x] = 1
        
        for a in A:
            for b in B:
                y = a+b
                if -y in dic:
                    count += dic[-y]
        
        return count