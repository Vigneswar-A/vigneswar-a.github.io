class UndergroundSystem:

    def __init__(self):
        self.checkin = {} #user - checkins
        self.journeys = defaultdict(list) #(start , end) - journey times
        self.counts = defaultdict(lambda : 0)

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.checkin[id] = (stationName , t)
        

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        station , time = self.checkin[id]
        del self.checkin[id]
        self.journeys[(station , stationName)].append(t - time)
        self.counts[(station , stationName)] += 1
        

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        return sum(self.journeys[(startStation , endStation)]) / self.counts[(startStation , endStation)]
        
        


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)