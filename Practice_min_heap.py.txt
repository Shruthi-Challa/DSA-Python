import heapq
"""

heap = []

heapq.heappush(heap,5)
heapq.heappush(heap,6)
heapq.heappush(heap,1)
heapq.heappush(heap,10)
print(heap)
print("smallest: ",heap[0])

while heap:
    print(heapq.heappop(heap))"""

#Create heap and insert
"""
heap = []

heapq.heappush(heap,7)
heapq.heappush(heap,5)
heapq.heappush(heap,11)
heapq.heappush(heap,2)
print(heap)
print("smallest :",heap[0])"""

#Using heapify

nums=[7,5,3,2,1]
heapq.heapify(nums)
print("Smallest :",nums[0])

while nums:
    print(heapq.heappop(nums)) #removing order