"""
LeetCode 200 - Number of Islands Solution
Author: Haris Kamal
Video Walkthrough: https://www.youtube.com/watch?v=O5k2tsp_pBA
"""

from typing import List


class Solution:
    """
    Solution 1: DFS
    Time Complexity: O(mn)
    Space Complexity: O(1)
    """

    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(row, col):
            if not (0 <= row < len(grid)) or not (0 <= col < len(grid[0])) or grid[row][col] == '0':
                return

            grid[row][col] = '0'

            dfs(row + 1, col)
            dfs(row - 1, col)
            dfs(row, col + 1)
            dfs(row, col - 1)

        count = 0

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == '1':
                    count += 1
                    dfs(row, col)

        return count
