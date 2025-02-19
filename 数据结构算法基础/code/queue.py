class Queue:
	"""队列"""
	def __init__(self):
		self.__list = []

	def enqueue(self, item):
		"""往队列中添加一个元素,入队"""
		self.__list.append(item)  # 1 时间复杂度 O(1) 
		# self.__list.insert(0, item) # 2 时间复杂度 O(n)

	def dequeue(self):
		"""从队列头部弹出一个元素，出队"""
		return self.__list.pop(0)  # 1 时间复杂度 O(n) 
		# return self.pop()   # 2 时间复杂度 O(1) 

	# 无论选择顺序表的哪一端出入，总有一个操作是O(n)
	# 需要看使用中入队和出队哪种操作更常用，再做选择

	def is_empty(self):
		"""判断队列是否为空"""
		return self.__list == []

	def size(self):
		"""返回队列的元素个数"""
		return len(self.__list)