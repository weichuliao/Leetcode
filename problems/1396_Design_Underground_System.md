Problem Link: https://leetcode.com/problems/design-underground-system/

## Solution I
two hash maps

```python
class UndergroundSystem:

    def __init__(self):
        # id -> [start_station, start_time]
        self.check_in_data = {}
        # (start_station, end_station) -> [total_time, total_trips]
        self.journey_data = defaultdict(lambda: [0, 0])

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.check_in_data[id] = [stationName, t]

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        start_station, start_time = self.check_in_data.pop(id)
        self.journey_data[(start_station, stationName)][0] += (t - start_time)
        self.journey_data[(start_station, stationName)][1] += 1

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        total_time, total_trips = self.journey_data[(startStation, endStation)]
        return total_time / total_trips


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)
```

#### Complexity Analysis:
- Time: $O(1)$ for all.
  - checkIn(...): $O(1)$
  - checkOut(...): $O(1)$
  - getAverageTime(...): $O(1)$
- Space: $O(P + S^2)$, where `S` is the number of stations on the network, and `P` is the number of passengers making a journey concurrently during peak time.
  - `check_in_data`: the maximum size of this hash map is the maximum possible number of people check-ined, which defined to be `P`.
  - `journey_data`: every possible pair of the `S` stations on the network to have an entry in this hash map, which would be $O(S^2)$.