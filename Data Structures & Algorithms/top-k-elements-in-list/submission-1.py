class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        freq = [[] for i in range(len(nums) + 1)] # create a bucket (empty list) for each number

        # for n in nums:
        #     count[n] = 1 + count.get(n, 0) # count frequency of each number
        for n, c in count.items():
            freq[c].append(n) # place numbers into buckets

        res = []
        
        # iterate from highest frequency to lowest
        for i in range(len(freq) - 1, 0, - 1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res