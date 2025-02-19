# BFS求解思路

1. 将起点坐标入队

2. 将队首结点可访问的点依次入队

3. 将队首结点出队
4. 重复2，3步骤，直到到达目标位置或队列为空。

**BFS搜到的结果一定是最短的。BFS运用到了队列。**



# 迷宫问题

### 代码实现

```c
using namespace std;
int a[100][100], v[100][100];
struct point  // 声明结构体point
{
	int x;
	int y;
	int step;
};
queue<point> r; // 申请队列r
// 定义四个方向，右下左上
int dx[4] = {0,1,0,-1};
int dy[4] = {1,0,-1,0};

int main()
{
	// 输入
	int n, m,startx,starty,endx,endy;
	scanf("%d%d",&n,&m);
	// 初始化迷宫数组，1表示空地，2表示障碍
	for(int i=1;i<=m;i++)
		for(int j=1;j<=n;j++)
			scanf("%d",&a[i][j]);  // 输入空地或障碍

	scanf("%d%d%d%d",&startx,&starty,&endx,&endy); // 输入起点坐标和终点坐标
    
	// BFS
	point start;  // 定义一个起点start（start为结构体类型）
	// 初始化start
	start.x = startx;
	start.y = starty;
	start.step = 0;
	r.push(start); // 将起点入队
	v[startx][starty] = 1;
	int flag = 0; // 判断是否有解
	// 若队列不为空
	while(!r.empty())
	{
		int x=r.front().x, y=r.front().y  // 取队首元素的x,y坐标
		if(x==endx && y==endy)
		{	
			flag = 1;  // 找到终点
			printf("%d", r.front().step); // 输出步数
			break；
		}
		// 遍历四个方向试探
		for(int k=0;k<=3;k++)
		{
			int tx, ty;  // 将要访问的位置
			tx = x + dx[k];
			ty = y + dy[k];
			// 判断该点是否为陆地，且未访问
			if(a[tx][ty] == 1 && v[tx][ty] == 0)
			{
				// 将该点入队 （需要放入结构体类型的位置）
				point temp;
				temp.x = tx;
				temp.y = ty;
				temp.step = r.front().step + 1;
				r.push(temp); // 入队
				v[tx][ty] = 1; // 该位置设为已访问
			}
		}
		r.pop(); // 四个方向拓展完了，需要将队首元素出队
	}
	if(flag == 0)
		printf("没有解");
	return 0;
}
```



