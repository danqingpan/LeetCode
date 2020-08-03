class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        
        b = set(bank)
        self.min_len = 9
        
        def recur(start, end, count, seen):
            if count > 8:
                return
            if start == end:
                if count < self.min_len:
                    self.min_len = count
                return
            for i in range(8):
                for s in 'ACGT':
                    new_s = start[:i] + s + start[i+1:]
                    if new_s not in seen and new_s in b:
                        seen.add(new_s)
                        recur(new_s, end, count+1,seen)
        
        recur(start, end, 0, set([start]))
        return self.min_len if self.min_len < 9 else -1
