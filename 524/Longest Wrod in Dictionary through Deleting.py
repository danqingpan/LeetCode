class Solution:
    def findLongestWord(self, s: str, d: List[str]) -> str:
        
        l = len(s)
        result = ''
        
        for item in d:
            m = len(item)
            if m <= l:
                i = 0
                j = 0
                while(i < l and j < m):
                    if s[i] == item[j]:
                        i += 1
                        j += 1
                    else:
                        i += 1
                if j == m:
                    if len(result) < len(item):
                        result = item
                    elif len(result) == len(item):
                        result = min(result, item)
                        
        return result