class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        graph = [[] for i in range(numCourses)]

        for course, prereq in prerequisites:
            graph[course].append(prereq)

        finished = set()
        path = set()

        def dfs(course):
            if course in path:
                return False
            
            if course in finished:
                return True
            
            path.add(course)
            for prereq in graph[course]:
                if not dfs(prereq):
                    return False
            
            path.remove(course)
            finished.add(course)

            return True


        for course in range(numCourses):
            if course not in finished:
                if not dfs(course):
                    return False


        return True




