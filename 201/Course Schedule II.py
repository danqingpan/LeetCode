class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        zero_inlet = set(range(numCourses))
        dic = collections.defaultdict(list)
        dep_count = collections.Counter()
        for c, dep in prerequisites:
            if c in zero_inlet: zero_inlet.remove(c)
            dic[dep].append(c)
            dep_count[c] += 1
        
        output = []
        zero_inlet = collections.deque(zero_inlet)
        while zero_inlet:
            node = zero_inlet.popleft()
            output.append(node)
            for target in dic[node]:
                dep_count[target] -= 1
                if dep_count[target] == 0: 
                    zero_inlet.append(target)
                    del dep_count[target]
        
        return output if not dep_count else []