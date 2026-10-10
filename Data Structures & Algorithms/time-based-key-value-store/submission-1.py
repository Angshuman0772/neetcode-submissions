class TimeMap:

    def __init__(self):
        self.TimeMap = {}   # key : value, time

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.TimeMap:
            self.TimeMap[key] = []
        self.TimeMap[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.TimeMap:
            return ""
        
        # self.TimeMap = "foo": [["bar", 1], ["baz", 3]] -> values = [["bar", 1], ["baz", 3]]
        valueTimePair = self.TimeMap[key]
        l = 0
        r = len(valueTimePair) - 1
        result = ""

        while l <= r:
            mid = (l + r) // 2

            # Given a timestamp, we want: the value whose timestamp is the largest ≤ given timestamp
            if valueTimePair[mid][1] <= timestamp:
                result = valueTimePair[mid][0]  # valid answer
                l = mid + 1             # try to find a later one
            else:
                r = mid - 1
            
            
        return result

