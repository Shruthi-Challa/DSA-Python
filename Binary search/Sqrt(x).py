class Solution(object):
    def mySqrt(self, x):
        if(x < 2):
            return x

        left = 0
        right = x

        while(left <= right):

            mid = left + (right - left)//2

            if mid*mid == x:
                return mid

            elif mid*mid >= x:
                right = mid-1

            else:
                left = mid+1

        return right
