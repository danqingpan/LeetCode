class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        
        people = sorted(people, key = lambda x: [-x[0], x[1]])
        
        for i in range(1,len(people)):
            temp = people[i]
            people.remove(temp)
            people.insert(temp[1],temp)
            
        return people