class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        queue = deque(["0000"])
        visited = set(deadends)
        
        moves = -1
        while queue:
            moves += 1
            # Check all cases with current number of moves
            for i in range(len(queue)):
                curr = queue.popleft()
                if curr in visited:
                    continue
                if curr == target:
                    return moves
                visited.add(curr)
                # There are 4 * 2 = 8 new code for every code with
                # one more move
                for i, letter in enumerate(curr):
                    digit = int(letter)
                    up = curr[:i] + str((digit + 1) % 10) + curr[i + 1:]
                    down = curr[:i] + str((digit - 1) % 10) + curr[i + 1:]
                    queue.append(up)
                    queue.append(down)
                        
        return -1