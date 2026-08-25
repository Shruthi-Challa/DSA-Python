class Solution(object):
    def shipWithinDays(self, weights, days):
        left = max(weights)
        right = sum(weights)

        while(left <= right):
            mid = left + (right - left )//2

            curr_load = 0
            used_days = 1
            
            for weight in weights:

                if curr_load + weight <= mid:
                    curr_load += weight

                else:
                    used_days +=1
                    curr_load = weight

            if used_days <= days:
                right = mid - 1

            else:
                left = mid + 1

        return left       