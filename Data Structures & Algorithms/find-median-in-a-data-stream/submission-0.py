class MedianFinder:

    def __init__(self):
        self.lower = []  # maxHeap (multiply by -1)
        self.upper = []  # minHeap

    def addNum(self, num: int) -> None:
        heapq.heappush(self.lower, -num)

        # Ensure every element in lower <= every element in upper
        if (self.lower and self.upper and
            -self.lower[0] > self.upper[0]):

            val = -heapq.heappop(self.lower)
            heapq.heappush(self.upper, val)

        # Rebalance heap sizes
        if len(self.lower) > len(self.upper) + 1:
            val = -heapq.heappop(self.lower)
            heapq.heappush(self.upper, val)

        if len(self.upper) > len(self.lower) + 1:
            val = heapq.heappop(self.upper)
            heapq.heappush(self.lower, -val)

    def findMedian(self) -> float:

        if (len(self.lower) + len(self.upper)) % 2 == 0:
            return (-self.lower[0] + self.upper[0]) / 2

        if len(self.lower) > len(self.upper):
            return -self.lower[0]
        
        if len(self.upper) > len(self.lower):
            return self.upper[0]