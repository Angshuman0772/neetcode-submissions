class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap = collections.defaultdict(list)
        for course, prereq in prerequisites:
            preMap[course].append(prereq)
        
        visited = set()

        def dfs(course):
            if course in visited:
                return False
            
            if preMap[course] == []:
                return True
            
            visited.add(course)
            # we recursively call dfs on every single prerequisite for this course. 
            # If even one prerequisite returns False (meaning it has a cycle), 
            # this current course cannot be finished, so we return False
            for prereq in preMap[course]:
                if not dfs(prereq):
                    return False
            
            visited.remove(course)
            preMap[course] = []
            return True
        
        for c in range(numCourses):
            if not dfs(c):
                return False
        
        return True