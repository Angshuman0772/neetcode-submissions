class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        minHeap = []

        for n, c in count.items():
            heapq.heappush(minHeap, [c, n])

            if len(minHeap) > k:
                heapq.heappop(minHeap)
            
        result = []
        for c, n in minHeap:
            result.append(n)
        
        return result