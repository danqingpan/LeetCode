class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        # zero_inlet holds initial nodes with zero inlet 
        zero_inlet = set(range(numCourses))
        # we use a dictionary dic to record dependencies
        dic = collections.defaultdict(list)
        # count the inlets of each node
        dep_count = collections.Counter()
        # initialize previous three data structure
        for c, dep in prerequisites:
            if c in zero_inlet: zero_inlet.remove(c)
            dic[dep].append(c)
            dep_count[c] += 1
        
        # use a list to record the result
        output = []
        # turn zero_inlet from set to queue (a list should also work)
        zero_inlet = collections.deque(zero_inlet)
        while zero_inlet:
            # pop a node
            node = zero_inlet.popleft()
            output.append(node)
            for target in dic[node]:
                # reduce inlet count by one because course node is recorded
                dep_count[target] -= 1
                # if inlet count is zero, we then add it to the queue
                if dep_count[target] == 0: 
                    zero_inlet.append(target)
                    del dep_count[target]
        
        return output if not dep_count else []
