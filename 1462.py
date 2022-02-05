# Problem Link: https://leetcode.com/problems/course-schedule-iv/
# Related to Floyd-Warshall
# Graph: https://leetcode-solution.cn/solutionDetail?type=2&id=2006&max_id=2007


# Solution:
# Runtime: 2204 ms, faster than 31.84% of Python3 online submissions for Course Schedule IV.
# Memory Usage: 17.3 MB, less than 98.05% of Python3 online submissions for Course Schedule IV.
class Solution:
    def Floyd_Warshall(self, dist, v):
        for k in range(v):
            for i in range(v):
                for j in range(v):
                    dist[i][j] = dist[i][j] or (dist[i][k] and dist[k][j])
        return dist
        
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        graph = [[False] * numCourses for _ in range(numCourses)]
        ans = []
        
        for fr, to in prerequisites:
            graph[fr][to] = True

        dist = self.Floyd_Warshall(graph, numCourses)
        
        for fr, to in queries:
            ans.append(bool(dist[fr][to]))
        
        return ans