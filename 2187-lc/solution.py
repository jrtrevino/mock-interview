from typing import List

class Solution:
    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        return None
    
if __name__ == "__main__":
    solution = Solution()
    time1 = [1,2,3]
    totalTrips1 = 5
    assert solution.minimumTime(time1, totalTrips1) == 3

    time2 = [2]
    totalTrips2 = 1
    assert solution.minimumTime(time1, totalTrips1) == 2
