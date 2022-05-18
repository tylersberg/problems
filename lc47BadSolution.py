from typing import List
# Given a collection of numbers, nums, that might contain duplicates, return all possible unique permutations in any order.


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        ans = set()

        # Implementation of Heap's algorithm, but there is a lot off wasted work with duplicate permutations.
        def makePerms(k, arr):
            if k == 1:
                ans.add(tuple(arr))
            else:
                makePerms(k-1, arr)
                for i in range(k-1):
                    if k % 2 == 0:
                        arr[i], arr[k-1] = arr[k-1], arr[i]
                    else:
                        arr[0], arr[k-1] = arr[k-1], arr[0]
                    makePerms(k-1, arr)
        makePerms(len(nums), nums)
        # Problem expects a List of Lists as solution.
        ansList = []
        for t in ans:
            ansList.append(list(t))
        return ansList


if __name__ == '__main__':
    s = Solution()
    nums = [1, 1, 2]
    print(s.permuteUnique(nums))
