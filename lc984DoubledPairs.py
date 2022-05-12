# Given an integer array of even length arr, return true if it is possible to reorder arr such that arr[2 * i + 1] = 2 * arr[2 * i] for every 0 <= i < len(arr) / 2, or false otherwise.
from collections import deque

class Solution(object):
    def canReorderDoubled(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        arr.sort()
        toMatch = arr[0]
        que = deque()
        i = 1
        while i < len(arr):
            if i + len(que) > len(arr):
                return False
            # Set target to valid match > than toMatch
            if toMatch < 0:
                if toMatch % 2 == 1:
                    return False
                target = toMatch/2
            elif toMatch == 0:
                target = 0
            else:
                target = toMatch*2
            # Handle value at index i
            if arr[i] > target:
                return False
            elif arr[i] < target:
                que.append(arr[i])
            else:
                if que:
                    toMatch = que.popleft()
                elif i == len(arr)-1:
                    return True
                else:
                    i += 1
                    toMatch = arr[i]
            i += 1
        return False
