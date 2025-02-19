// DFS

using namespace std;
int m, n // m*n数组
int startx, starty  // 起点位置
int endx ,endy;  // 终点位置
int min=99999999 // 最短路径的步数
int a[100][100]  // 迷宫数组，1表示空地，2表示障碍
int v[100][100]  // 访问数组，0表示未访问，1表示已访问

void dfs(int x, int y, int step)  // x, y当前坐标，step当前所走步数
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
		v[x][y+1]=0;  // 标记为未访问，然后回溯（因为已访问过的点是不能再访问的）
	}
	// 往下
	if(a[x+1][y]==1 && v[x+1][y]==0)
	{
		v[x+1][y]=1;  // 标记为已访问
		dfs(x+1, y, step+1); // dfs搜索，传入的步数+1
		v[x+1][y]=0;  // 标记为未访问，然后回溯（因为已访问过的点是不能再访问的）
	}
	// 往左
	if(a[x][y-1]==1 && v[x][y-1]==0)
	{
		v[x][y-1]=1;  // 标记为已访问
		dfs(x, y-1, step+1); // dfs搜索，传入的步数+1
		v[x][y-1]=0;  // 标记为未访问，然后回溯（因为已访问过的点是不能再访问的）
	}
	// 往上
	if(a[x-1][y]==1 && v[x-1][y]==0)
	{
		v[x-1][y]=1;  // 标记为已访问
		dfs(x-1, y, step+1); // dfs搜索，传入的步数+1
		v[x-1][y]=0;  // 标记为未访问，然后回溯（因为已访问过的点是不能再访问的）
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
 



// BFS
using namespace std;
int a[100][100], v[100][100];
struct point
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
	// v[startx][starty] = 1; //初始位置，设为已访问
	
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


