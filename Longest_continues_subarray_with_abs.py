class Solution(object):
    def longestSubarray(self, nums, limit):
        res = 0 

        left = 0

        currmax = collections.deque()
        currmin = collections.deque()

        for right in range(len(nums)):

            while currmax and nums[currmax[-1]] < nums[right]:
                currmax.pop()
            currmax.append(right)

            while currmin and nums[currmin[-1]] > nums[right]:
                currmin.pop()
            currmin.append(right)

            while nums[currmax[0]]-nums[currmin[0]] > limit:

                if currmax[0] == left:
                    currmax.popleft()

                if currmin[0]==left:
                    currmin.popleft()

                left+=1
            res = max(res,right-left+1)

        return res
