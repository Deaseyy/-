# BFS

队列实现

![image-20200920165325794](C:\Users\12395\AppData\Roaming\Typora\typora-user-images\image-20200920165325794.png)

选定一个根节点n，遍历与自己最近的所有结点n1，再分别遍历每个n1的所有邻结点(为被搜索过的结点)，一层一层遍历下去；但对同一层结点的邻接点遍历时，应遵循先进先出的原则（保证层的顺序），如上图：

- A  B C  D E F  , queue存放待搜索的结点, 选取A为根节点queue=[A]，

  - 1.取出A,查找A的邻结点：先B，后C，queue=[B,C];
  - 2.取出B,查找B的邻结点：D，queue=[C,D]
  - 3.取出C,查找C的邻结点：E，queue=[D,E]
  - 4.取出D,查找D的邻结点：F，queue=[E,F]
  - 5.取出E,F,都没有邻结点，搜索完毕

  第2步和第3步顺序不能调换，需符合上一步搜索的顺序，否则就不是BFS





# DFS

栈实现







# Dijkstra

求最短路径

![image-20200921224901897](C:\Users\12395\AppData\Roaming\Typora\typora-user-images\image-20200921224901897.png)

