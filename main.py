class Solution(object):
    def firstBadVersion(self, n):
        left = 1
        right = n
        if isBadVersion(1):
            return 1
        while left < right:
            if isBadVersion(right):
                if isBadVersion(right - 1):
                    right -= 1
                else:
                    return right