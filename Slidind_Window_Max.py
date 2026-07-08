class Solution(object):
    def maxSlidingWindow(self, nums, k):
        deque = []
        res = []

        for right in range(len(nums)):
            left = right - k + 1

            if deque and deque[0] < left:
                deque.pop(0)

            while deque and nums[deque[-1]] < nums[right]:
                deque.pop()

            deque.append(right)

            if right >= k - 1:
                res.append(nums[deque[0]])
        return res
