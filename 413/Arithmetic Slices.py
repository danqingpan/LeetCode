class Solution:
    def numberOfArithmeticSlices(self, A: List[int]) -> int:
        
        if len(A) < 3:
            return 0
        
        slices = []
        
        prev_gap = A[1] - A[0]
        current_gap = None
        
        count = 0
        for i in range(1,len(A)-1):
            current_gap = A[i+1] - A[i]
            if current_gap == prev_gap and i != len(A) - 2:
                count += 1
            elif current_gap == prev_gap:
                count += 1
                slices.append(count)
            else:
                prev_gap = current_gap
                slices.append(count)
                count = 0
                
        result = 0

        for item in slices:
            result += int(item*(item+1)/2)
        return result