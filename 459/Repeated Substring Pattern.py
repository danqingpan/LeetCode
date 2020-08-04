class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        s_set = set(s)
        l = len(s)
        
        for i in range(l//2):
            if s[i] in s_set:
                s_set.remove(s[i])
            if not s_set:
                if l%(i+1) == 0:
                    if s == s[:i+1]*(l//(i+1)):
                        return True                
        return False