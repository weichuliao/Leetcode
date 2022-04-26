from typing import List

class Solution:
    def findDataLocations(self, locations: List[int], movedFrom: List[int], movedTo: List[int]) -> List[int]:
        # convert locations to set
        sets = set()
        for location in locations:
            sets.add(location)
        print(sets)

        # iterate through movedFrom (same length as movedTo) and change the locations
        for i in range(len(movedFrom)):
            sets.remove(movedFrom[i])
            sets.add(movedTo[i])
        print(sets)

        # convert locations back to list and return
        return sorted(list(sets))

execution = Solution()
result = execution.findDataLocations([100, 1, 9, 7, 6, 8, 2], [100, 7, 2, 5], [5, 3, 20, 4])
print('The answer is', result)