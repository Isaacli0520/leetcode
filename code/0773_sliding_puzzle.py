class Solution:
    # BFS
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        queue = deque(["".join([str(i) for i in board[0]] + [str(j) for j in board[1]])])
        d = [
            [1, 3],
            [0, 2, 4],
            [1, 5],
            [0, 4],
            [1, 3, 5],
            [2, 4],
        ]
        moves = -1
        visited = set()
        while queue:
            moves += 1
            for i in range(len(queue)):
                curr = queue.popleft()
                if curr in visited:
                    continue
                visited.add(curr)
                if curr == "123450":
                    return moves
                idx = curr.find("0")
                for j in d[idx]:
                    tmp = curr.replace("0", curr[j])
                    tmp = tmp[:j] + "0" + tmp[j + 1:]
                    queue.append(tmp)
                
        return -1
            
            