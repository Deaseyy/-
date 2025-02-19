class Deque:
	"""双端队列"""
	def __init__(self):
		self.__list = []

	def add_front(self, item):
		"""从头部往队列中添加一个元素"""
		self.__list.insert(0, item)

	def add_rear(self, item):
		"""从尾部往队列中添加一个元素"""
		self.__list.append(item)

	def pop_front(self):
		"""从队列头部弹出一个元素"""
		return self.__list.pop(0)  

	def pop_rear(self):
		"""从队列尾部弹出一个元素"""
		return self.__list.pop()  

	def is_empty(self):
		"""判断队列是否为空"""
		return self.__list == []

	def size(self):
		"""返回队列的元素个数"""
		return len(self.__list)