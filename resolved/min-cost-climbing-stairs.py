#-*- coding: utf-8 -*-

class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        # special input
        if 1 == len(cost):
            return 0

        # init status 起始条件
        best_map = {0: cost[0], 1: cost[1]}

        # iteration 迭代
        for i in range(2, len(cost)):
            best_map[i] = min(best_map[i-1], best_map[i-2]) + cost[i]
            
        # inferior strategy 劣势策略舍弃
        # final status 终结条件
        return min(best_map[len(cost)-1], best_map[len(cost)-2])

if "__main__" == __name__:
    s = Solution()
    print s.minCostClimbingStairs([1])  # 0
    print s.minCostClimbingStairs([2, 1])  # 1
    print s.minCostClimbingStairs([1, 100, 1, 1])  # 2
    print s.minCostClimbingStairs([1, 100, 100, 2, 1, 1])  # 102
    print s.minCostClimbingStairs([3, 100, 100, 2, 1, 1])  # 103
    print s.minCostClimbingStairs([1, 100, 100, 3, 1, 1, 1])  # 103
