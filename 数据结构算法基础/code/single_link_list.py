class Node:
	def __init__(self, item):
		self.elem = item
		self.next = None


class SingleLinkList：
	"""单链表"""
	def __init__(self, node=None):
		self.__head = node
	
	def is_empty(self):
		"""链表是否为空"""
		return self.__head == None

	def length(self):
		"""链表长度"""
		# cur游标，用来移动遍历结点
		cur = self.__head
		# count记录数量
		count = 0
		while cur != None:
			count += 1
			cur = cur.next
		return count

	def travel(self):
		"""遍历整个链表"""
		cur = self.__head
		while cur != None:
			print(cur.elem, end=" ")
			cur = cur.next
		print("")

	def add(self, item):
		"""链表头部添加元素，头插法"""
		node = Node(item)
		node.next = self.__head
		self.__head = node   # 新插入的结点作为头结点

	def append(self, item):
		"""链表尾部添加元素，尾插法"""
		node = Node(item)
		if self.is_empty():
			self.__head = node
		else:
			cur = self.__head
			while cur.next != None:
				cur = cur.next
			cur.next = node

	def insert(self, pos, item):
		"""指定位置添加元素
		：params pos 从0开始
		"""
		if pos <= 0:
			self.add(item)
		elif pos > (self.length()-1):
			self.append(item)
		else:
			pre = self.__head
			count = 0
			while count < (pos-1):
				count += 1
				pre = pre.next
			# 当退出循环后，pre指向pos-1位置
			node = Node(item)
			node.next = pre.next
			pre.next = node

	def remove(self, item):
		"""删除结点"""
		cur = self.__head
		pre = None
		while cur != None:
			if cur.elem == item:
				# 先判断此节点是否是头结点
				if cur == self.__head:
					self.__head = cur.next
				else:
					pre.next = cur.next
				break
			else:
				pre = cur
				cur = cur.next

	def search(self, item):
		"""查找结点"""
		cur = self.__head
		while cur != None:
			 if cur.elem == item:
			 	return True
			 else:
			 	cur = cur.next	
		return False		


