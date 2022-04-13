class Solution:
    # Dijikstra
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        graph = [[] for _ in range(n)]
        for i, (a, b) in enumerate(edges):
            graph[a].append((b, 1 / succProb[i]))
            graph[b].append((a, 1 / succProb[i]))
            
        heap = [(1, start)]
        dist = {}
        heapq.heapify(heap)
        while heap:
            prob, curr = heapq.heappop(heap)
            if curr not in dist:
                dist[curr] = prob
                for node, weight in graph[curr]:
                    heapq.heappush(heap, (prob * weight, node))
        return 1 / dist[end] if end in dist else 0