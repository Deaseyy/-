# 一，图

## 求解思路

### 原理

从某点出发，沿着一个方向往下试探，当找到目标位置，还需要回溯，以便找到所有的路径，再比较最短的路径。

**特点**：比较盲目，效率没有BFS高。DFS运用到了栈。

### 思路

1.先判断是否到达目标位置，如果到达目标位置，再试探有无其它更短的路径

2.如果没有到达目标位置，则找到下一步可以到达的位置，直到找到目标位置

### 框架

网格 DFS 遍历的框架代码

```java
void dfs(int[][] grid, int r, int c) {
    // 判断 base case
    // 如果坐标 (r, c) 超出了网格范围，直接返回
    if (!inArea(grid, r, c)) {
        return;
    }
    // 访问上、下、左、右四个相邻结点
    dfs(grid, r - 1, c);
    dfs(grid, r + 1, c);
    dfs(grid, r, c - 1);
    dfs(grid, r, c + 1);
}

// 判断坐标 (r, c) 是否在网格中
boolean inArea(int[][] grid, int r, int c) {
    return 0 <= r && r < grid.length 
        	&& 0 <= c && c < grid[0].length;
}
```



## 迷宫问题

### 求解思路

1. 判断当前位置是否为目标位置

   - 若是：更新最短步数

   - 回溯

2. 继续按顺时针试探其它方向，右下左上

3. 到达下一个可到达位置

   - 将该位置标为 已访问
   - dfs搜索
   - 回溯，将该位置标为 未访问



### 实现代码

```c
using namespace std;
int m, n // m*n数组
int startx, starty  // 起点位置
int endx ,endy;  // 终点位置
int min=99999999 // 最短路径的步数
int a[100][100]  // 迷宫数组，1表示空地，2表示障碍
int v[100][100]  // 访问数组，0表示未访问，1表示已访问

// x, y当前坐标，step当前所走步数
void dfs(int x, int y, int step)  
{	
	// 判断当前位置是否为终点
	if(x==endx && y==endy)  
	{
		if(step<min)
			min=step;  // 更新最短步数
		return; // 回溯
	}
	// 顺时针试探：右下左上（根据起点和终点的相对位置来定义）
	// 往右，若该点为空地，且未访问
	if(a[x][y+1]==1 && v[x][y+1]==0)
	{
		v[x][y+1]=1;  // 标记为已访问
		dfs(x, y+1, step+1); // dfs搜索，传入的步数+1
		v[x][y+1]=0;  // 回溯，标记为未访问（因为已访问过的点是不能再访问的）
	}
	// 往下
	if(a[x+1][y]==1 && v[x+1][y]==0)
	{
		v[x+1][y]=1;  
		dfs(x+1, y, step+1); 
		v[x+1][y]=0;
	}
	// 往左
	if(a[x][y-1]==1 && v[x][y-1]==0)
	{
		v[x][y-1]=1; 
		dfs(x, y-1, step+1);
		v[x][y-1]=0;
	}
	// 往上
	if(a[x-1][y]==1 && v[x-1][y]==0)
	{
		v[x-1][y]=1;
		dfs(x-1, y, step+1);
		v[x-1][y]=0;
	}
	return; // 返回，即回溯
}


int main()
{
	int startx, starty;
	scanf("%d%d", &m,&n); // 输入m*n的数组
	// 初始化迷宫数组，1表示空地，2表示障碍
	for(int i=1;i<=m;i++)
		for(int j=1;j<=n;j++)
			scanf("%d",&a[i][j]);  // 输入空地或障碍

	scanf("%d%d%d%d",&startx,&starty,&endx,&endy); // 输入起点坐标和终点坐标
	v[startx][starty] = 1; //初始位置，设为已访问
	dfs(startx, starty, 0);
	printf("%d", min)  // 打印结果
	return 0;
}
```



### 简化代码

```c
// 简化代码, 使用for循环四个方向
// 定义方向：右(x+0,y+1)，下(x+1,y+0), 左(x+0, y-1), 上(x-1, y+0)
int dx[4]={0,1,0,-1}; 
int dy[4]={1,0,-1,0};

for (int k = 0; k <= 3; k++)
{
	int tx,ty; // 下次试探的位置
	tx=x+dx[k];
	ty=y+dy[k];
	if(a[tx][ty]==1 && v[tx][ty]==0)
	{
		v[tx][ty] = 1;
		dfs(tx, ty, step+1);
		v[tx][ty] = 0;
	}
}
```



# 二，树

## 求解步骤

### 自下而上型

1.子问题，通常找一个中间状态来推断

2.向子问题要答案

- dfs(node.left) 和 dfs.(node.right)

3.利用子问题的答案构建当前问题(当前递归层)的答案

4.若有必要，做一些额外操作

5.返回答案, 给父问题

**注意**：**2 和 5 中，答案的物理意义要一样**

### 自上而下型

1.子问题

2.利用父问题传下来的值做一些计算

3.若有必要，做一些额外操作

4.把值传下去给子问题继续递归

**注意：自上而下，只是把值向下传递，通常没有返回值**



## 例题

### [104. 二叉树的最大深度](https://leetcode-cn.com/problems/maximum-depth-of-binary-tree/)

**自下而上型**

1.子问题 ——> node == null,return res

2.向子问题要答案

- 最大深度

3.利用子问题的答案构建当前问题(当前递归层)的答案

- 左子树和右子树深度的最大值+1：max(left_ans, right_ans) + 1

4.若有必要，做一些额外操作

5.返回答案，给父问题

**实现代码：**

```python
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        # 左子树的最大距离和右子树的最大距离的最大值 + 1
        dep = 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
        return dep
```

### [124. 二叉树中的最大路径和](https://leetcode-cn.com/problems/binary-tree-maximum-path-sum/)

**自下而上型**

给定一个**非空**二叉树，返回其最大路径和。

![image-20201212143917700](C:\Users\12395\AppData\Roaming\Typora\typora-user-images\image-20201212143917700.png)

1.子问题 

2.向子问题要答案

- 从根到叶路径的最大和（直上直下型路径）

3.利用子问题的答案构建当前问题(当前递归层)的答案

- 左子树和右子树的最大路径和(不能为负)：max(left, right, 0) + node.val

  如果左右路径和小于0，则不如舍弃，取自身就行；

4.若有必要，做一些额外操作

- 用一个变量保存当前最大完整路径和（人字形路径）

  curr_sum = max(left, 0) + max(right, 0) + node.val

  global_max = max(global_max, curr_sum)

  因为最终返回的答案不一定是想要的最优解(可能树的另一边或父节点为负)，所以需要一个全局变量，保存当前的最大路径和（人字形）；

5.返回答案，给父问题

- 必须也为（直上直下型路径）

**实现代码:**

```python
class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.max_sum = float('-inf')
        self.dfs(root)
        return self.max_sum
    
    def dfs(self, node):
        if not node:
            return 0
        
        # 子问题:左子树最大路径和(直上直下型) 与 右子树最大路径和的最大值，若小于零则舍弃，取0
        left_sum = self.dfs(node.left)
        right_sum = self.dfs(node.right)

        # 保存当前最大路径和（完整人字形），因最终的递归返回不一定是最优解
        curr_sum = max(left_sum, 0) + max(right_sum, 0) + node.val
        self.max_sum = max(self.max_sum, curr_sum)
        # 构建当前问题的答案返回
        return max(left_sum, right_sum, 0) + node.val  
```



### [129. 求根到叶子节点数字之和](https://leetcode-cn.com/problems/sum-root-to-leaf-numbers/)

**自上而下型**

给定一个二叉树，它的每个结点都存放一个 0-9 的数字，每条从根到叶子节点的路径都代表一个数字。例如，从根到叶子节点路径 1->2->3 代表数字 123。

计算从根到叶子节点生成的所有数字之和。

1.子问题

- 叶子节点

2.利用父问题传下来的值做一些计算

- 拼接数字：num = num*10 + node.val

3.若有必要，做一些额外操作

- global_sum += num

4.把值传下去给子问题继续递归

- dfs(node, num)

**实现代码：**

```python
class Solution(object):
    def sumNumbers(self, root):
        self.total_sum = 0
        self.dfs(root, 0)
        return self.total_sum

    def dfs(self, node, num):
        if not node:
            return
        
        # 拼接成数字，利用数学方法
        num = num*10 + node.val
        # 判断叶子节点，若是，则已经是完整路径，将数字加到总和
        if not node.left and not node.right:
            self.total_sum += num
            return

        # 将num值继续传下去
        if node.left:
            self.dfs(node.left, num)
        if node.right:
            self.dfs(node.right, num)
```



**更多题目：**

98  110  113  236*  450  508



# 三，图的dfs题目

### 1.岛屿问题

#### [200. 岛屿数量](https://leetcode-cn.com/problems/number-of-islands/)

给你一个由 '1'（陆地）和 '0'（水）组成的的二维网格，请你计算网格中岛屿的数量。岛屿总是被水包围，并且每座岛屿只能由水平方向和/或竖直方向上相邻的陆地连接形成。

```python
class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        m = len(grid)
        n = len(grid[0])
        island = 0  # 岛屿数量

        def dfs(row, col):
            """dfs 将相连的所有岛屿忽略掉(变为'0')"""
            # 边界
            if row < 0 or row >=m or col < 0 or col >= n or grid[row][col] == '0':
                return

            grid[row][col] = '0'
            dfs(row-1, col)
            dfs(row, col+1)
            dfs(row+1, col)
            dfs(row, col-1)

        for row in range(m):
            for col in range(n):
                if grid[row][col] == '1':
                    island += 1
                    dfs(row, col)
        return island
```

#### [695. 岛屿的最大面积](https://leetcode-cn.com/problems/max-area-of-island/)

```python
class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid)
        n = len(grid[0])
        self.max_area = 0 # 记录最大岛屿的面积
        self.area = 0 # 记录当前岛屿的面积

        def dfs(row, col):
            # 边界
            if row < 0 or row >=m or col < 0 or col >= n or grid[row][col] == 0:
                return
            
            grid[row][col] = 0 # 将访问过的陆地沉没，变为0
            self.area += 1
            dfs(row-1, col)
            dfs(row, col+1)
            dfs(row+1, col)
            dfs(row, col-1)
            
        for row in range(m):
            for col in range(n):
                if grid[row][col] == 1: # 提前判断退出，避免每次循环进入dfs判断多个边界
                    dfs(row, col)
                    self.max_area = max(self.max_area, self.area)
                    self.area = 0 # 当前面积清0
        
        return self.max_area
```



# 四，树的dfs题目