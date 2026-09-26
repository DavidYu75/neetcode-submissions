class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency_table = {}

        for num in nums:
            frequency_table[num] = 1 + frequency_table.get(num, 0)

        heap = []

        for num in frequency_table.keys():
            heapq.heappush(heap, (frequency_table[num], num))

            if len(heap) > k:
                heapq.heappop(heap)

        result = []

        for i in range(k):
            result.append(heapq.heappop(heap)[1])

        return result