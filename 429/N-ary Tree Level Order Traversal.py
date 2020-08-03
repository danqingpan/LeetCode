"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root:
            return []
        
        queue_a = [root]
         result = []
        
        while(queue_a):
            temp_queue = []
            result.append([])
            for node in queue_a:
                result[-1].append(node.val)
                temp_queue.extend(node.children)
                
            queue_a = temp_queue.copy()
        
        return result
        
            