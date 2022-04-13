class Solution:
    # Dijkstra
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = [[] for i in range(n + 1)]
        for u, v, weight in times:
            graph[u].append((v, weight))
        
        dist = {}
        heap = [(0, k)]
        heapq.heapify(heap)
        while heap:
            time, curr = heapq.heappop(heap)
            if curr not in dist:
                dist[curr] = time
                for node, weight in graph[curr]:
                    heapq.heappush(heap, (dist[curr] + weight, node))
        if len(dist) != n:
            return -1
        return max(dist.values())