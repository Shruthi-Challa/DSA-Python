class Solution(object):
    def lastStoneWeight(self, stones):
        heap = []

        for s in stones:
            heapq.heappush(heap,-s)
        

        while len(heap)>1:
            first = -heapq.heappop(heap)
            second = -heapq.heappop(heap)

            if first != second:
                heapq.heappush(heap,-(first-second))

        if heap:
            return -heap[0]

        else:
            return 0