class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        #tree
        #what causes something to be false
        # loop
        #two pointers? doesnt seem right
        #could use a hash set to see if pre reqs was something highlighted, but doesnt seem right
        #
        #something with numcourses and hashset?
        #you return false when you detect that its not a topical graph, and is a cycle
        #therefore its a cycle detection problem
        # directed graph cycle detection of l >= 0

        graph = [[] for i in range(numCourses)]
        for course, prereq in prerequisites:
            graph[course].append(prereq)

        path = set()
        finished = set()

        def dfs(course):
            if course in finished:
                return True
            
            if course in path:
                return False
            
            path.add(course)
            for prereq in graph[course]:
                if not dfs(prereq):
                    return False
            
            finished.add(course)
            path.remove(course)
            return True
        
        for course in range(numCourses):
            if course not in finished:
                if not dfs(course):
                    return False
        
        return True





