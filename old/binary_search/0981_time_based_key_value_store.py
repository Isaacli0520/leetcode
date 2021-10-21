class TimeMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.d = collections.defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.d[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        left, right = 0, len(self.d[key])
        while left < right:
            mid = left + (right - left) // 2
            if self.d[key][mid][1] <= timestamp:
                left = mid + 1
            else:
                right = mid
        
        return "" if left == 0 else self.d[key][left - 1][0]
        
                
                
# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)