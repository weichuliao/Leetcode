# Problem Link: https://leetcode.com/problems/network-delay-time/


# Solution:
# Runtime: 921 ms, faster than 17.41% of Python3 online submissions for Network Delay Time.
# Memory Usage: 16.2 MB, less than 48.85% of Python3 online submissions for Network Delay Time.
class Solution:
    def dijkstra(self, graph, start, end):
        heap = [(0, start)]
        visited = set()
        while heap:
            (cost, u) = heapq.heappop(heap)
            if u in visited:
                continue
            visited.add(u)
            if u == end:
                return cost
            for v, c in graph[u]:
                if v in visited:
                    continue
                next = cost + c
                heapq.heappush(heap, (next, v))
        return -1
    
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = collections.defaultdict(list)
        for fr, to, w in times:
            graph[fr-1].append((to-1, w))
        ans = -1
        for to in range(n):
            dist = self.dijkstra(graph, k-1, to)
            if dist == -1:
                return -1
            ans = max(ans, dist)
        return ans