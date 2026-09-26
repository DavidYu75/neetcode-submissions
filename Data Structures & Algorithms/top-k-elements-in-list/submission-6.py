class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency_table = {}

        for i in range(len(nums)):
            frequency_table[nums[i]] = 1 + frequency_table.get(nums[i], 0)

        heap = []

        for num in frequency_table.keys():
            heapq.heappush(heap, (frequency_table[num], num))

            if len(heap) > k:
                heapq.heappop(heap)
        
        result = []

        for i in range(k):
            number = heapq.heappop(heap)[1]
            result.append(number)

        return result