class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        
        b = set(bank)
        result = []
        
        def recur(start, end, count, seen):
            if count > 8:
                return
            if start == end:
                result.append(count)
                return
            for i in range(8):
                for s in 'ACGT':
                    new_s = start[:i] + s + start[i+1:]
                    if new_s not in seen and new_s in b:
                        seen.add(new_s)
                        recur(new_s, end, count+1,seen)
        
        recur(start, end, 0, set([start]))
        if result: return min(result)
        else: return -1
