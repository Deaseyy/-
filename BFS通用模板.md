### 模板

```
BFS 使用队列，把每个还没有搜索到的点依次放入队列，然后再弹出队列的头部元素当做当前遍历点。BFS 总共有两个模板：
```

**不需要确定当前遍历到了哪一层，BFS 模板如下:**

```python
while queue 不空：
    cur = queue.pop()
    for 节点 in cur的所有相邻节点：
        if 该节点有效且未访问过： # 一般会定义一个访问数组visited
            queue.push(该节点)
```



**若要确定当前遍历到了哪一层，BFS 模板如下:**
这里增加了 level 表示当前遍历到二叉树中的哪一层了，也可以理解为在一个图中，现在已经走了多少步了。size 表示在当前遍历层有多少个元素，也就是队列中的元素数，我们把这些元素一次性遍历完，即把当前层的所有元素都向外走了一步。

```
level = 0
while queue 不空：
    size = queue.size()
    while (size --) {
        cur = queue.pop()
        for 节点 in cur的所有相邻节点：
            if 该节点有效且未被访问过：
                queue.push(该节点)
    }
    level ++;
```

**个人理解：当节点被刚加入到队列时，还不能算遍历到该节点；只有当节点从队列中取出来时，此时该节点才是当前遍历元素，可以对该节点进行处理。 **



### 例题

#### [542. 01 矩阵](https://leetcode-cn.com/problems/01-matrix/)

给定一个由 0 和 1 组成的矩阵，找出每个元素到最近的 0 的距离。两个相邻元素间的距离为 1 。

```python
class Solution:
    def updateMatrix(self, matrix):	
        """
        从1开始找，遇到0停止的话，最后找到的结果是离这个0最近的1，而题目要求的是离1最近的0，归根结底还		  是因为“多源BFS是从所有可能的起点开始找的
        """
    	m = len(matrix)
        n = len(matrix[0])
        res = [[0] * n for _ in range(m)] # 结果集
        visited = [[0] * n for _ in range(m)] # 访问数组
        queue = []
        for x in range(m):
            for y in range(n):
                if matrix[x][y] == 0: # 将题目转换为 0 到 1 的距离
                    queue.append((x, y))
                    visited[x][y] = 1
        step = 0 # 层级，这里也能代表路径
        while queue:
            size = len(queue)
            for i in range(size):
                x, y = queue.pop(0)
                if matrix[x][y] == 1:
                    # 处理当前遍历节点
                    # 搜索到1后，则路径即为当前层级数()
                    res[x][y] = step

                if x-1 >= 0 and visited[x-1][y] == 0:
                    queue.append((x-1, y))
                    visited[x - 1][y] = 1
                if y+1 < n and visited[x][y+1] == 0:
                    queue.append((x, y+1))
                    visited[x][y + 1] = 1
                if x+1 < m and visited[x+1][y] == 0:
                    queue.append((x+1, y))
                    visited[x + 1][y] = 1
                if y-1 >= 0 and visited[x][y-1] == 0:
                    queue.append((x, y-1))
                    visited[x][y - 1] = 1
            step += 1 # 搜索层级，即最短路径
        return res
```

