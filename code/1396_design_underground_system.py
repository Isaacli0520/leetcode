class UndergroundSystem:

    def __init__(self):
        self.record = collections.defaultdict(int)
        self.count = collections.defaultdict(int)
        self.ids = {}

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.ids[id] = (stationName, t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        start_station, time = self.ids.pop(id)
        self.record[start_station + '-' + stationName] += (t - time)
        self.count[start_station + '-' + stationName] += 1

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        return 1.0 * self.record[startStation + '-' + endStation] / self.count[startStation + '-' + endStation]


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)