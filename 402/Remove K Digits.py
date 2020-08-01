class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        
        if k == 0 or not num:
            return num
        if k >= len(num):
            return '0'

        mono_stack = []

        c = 0
        for i in range(len(num)):
            if c < k:
                while len(mono_stack) > 0 and int(num[i]) < int(mono_stack[-1]):
                    mono_stack.pop()
                    c += 1
                    if c == k:
                        break
            mono_stack.append(num[i])
        
        return str(int(''.join(mono_stack)))[:len(mono_stack)-k+c]
