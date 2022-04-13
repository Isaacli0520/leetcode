class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = [[] for _ in range(n)]
        for a, b, price in flights:
            graph[a].append((b, price))
        
        heap = [(0, -1, src)]
        heapq.heapify(heap)
        dist = {}
        while heap:
            price, stop, curr = heapq.heappop(heap)
            if curr == dst:
                return price
            # Will consider if stop < k and if there is already a shortest
            # path to curr, the new path must either have fewer stops or
            # a cheaper price (Since we use a min-heap, if dist in curr,
            # it must have a smaller price so the new path can never have
            # a cheaper price)
            if stop < k and (curr not in dist or (curr in dist and stop < dist[curr])):
                dist[curr] = stop
                for node, price2 in graph[curr]:
                    heapq.heappush(heap, (price + price2, stop + 1, node))
        
        return -1