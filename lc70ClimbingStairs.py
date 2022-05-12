# You are climbing a staircase. It takes n steps to reach the top.
# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
from math import comb

class Solution:
    def climbStairs(self, n: int) -> int:
        tot = 1
        for i in range(1, n//2+1):
            tot += comb(n-i, i)
        return tot
