class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        arr = []
        graph = [[] for i in range(numCourses)]
        indegree = [0] * numCourses
        for course, prereq in prerequisites:
            graph[prereq].append(course)
            indegree[course] += 1

        q = deque()
        for course, deg in enumerate(indegree):
            if deg == 0:
                q.append(course)

        while q:
            prereq = q.popleft()
            arr.append(prereq)

            for course in graph[prereq]:
                indegree[course] -= 1
                if indegree[course] == 0:
                    q.append(course)

        return arr if len(arr) == numCourses else []