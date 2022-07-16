class Solution:
    # The robot stays in the circle if and only if 
    # it changes direction (ie. doesn't stay pointing north)
    # or it moves 0.
    def isRobotBounded(self, instructions: str) -> bool:
        # 0 up 1 right 2 down 3 left
        dd = {
            0: (0, 1),
            1: (1, 0),
            2: (0, -1),
            3: (-1, 0)
        }
        x, y = 0, 0
        d = 0
        for i in instructions:
            if i == "G":
                delta = dd[d]
                x += delta[0]
                y += delta[1]
            elif i == "L":
                d -= 1
                if d < 0:
                    d = 3
            elif i == "R":
                d += 1
                if d > 3:
                    d = 0
        return (x == 0 and y == 0) or d != 0
        