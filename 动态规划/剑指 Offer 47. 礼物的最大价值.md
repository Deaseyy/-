### 剑指 Offer 47. 礼物的最大价值
在一个 m*n 的棋盘的每一格都放有一个礼物，每个礼物都有一定的价值（价值大于 0）。
你可以从棋盘的左上角开始拿格子里的礼物，并每次向右或者向下移动一格、直到到达棋盘的右下角。
给定一个棋盘及其上面的礼物的价值，请计算你最多能拿到多少价值的礼物？

##### 求最值型动态规划


```python
class Solution(object):
    def maxValue(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        # 最后一步：前一步为(m-1, n-2)或(m-2,n-1)
        # 子问题:走到(m-1, n-2)或(m-2,n-1)，分别最多拿到多少价值的礼物；
        # 因为必须要最多价值，所以前一步也要是当前步最多价值，即max{f(m-1, n-2), f(m-2,n-1)}
        # 原问题：到达棋盘右下角(m-1,n-1)，最多拿到多少价值的礼物
        # 设状态：f[i][j] = 达到(i,j)位置，最多拿到多少价值礼物
        # 转移方程：f[i][j] = max{f(i, j-1)+grid[i][j], f(i-1, j)+grid[i][j]}
        m = len(grid)  # 行
        n = len(grid[0]) # 列
        f = [[0] * n for i in range(m)]

        for i in range(0, m):
            for j in range(0, n):
                if i == 0 and j == 0:
                    f[0][0] = grid[0][0]  # 初始化f
                    continue

                if i == 0:
                    f[i][j] = f[i][j-1] + grid[i][j]  # 左边位置的礼物价值+当前位置价值
                elif j == 0:
                    f[i][j] = f[i-1][j] + grid[i][j]  # 上边位置的礼物价值+当前位置价值
                else:
                    f[i][j] = max(f[i][j-1] + grid[i][j], f[i-1][j] + grid[i][j])

        return f[m-1][n-1]      
```
