arr = [6,3,2,4,5,9,5,1,7,4]

# def bubble_sort(li):
# 	for i in range(len(li)-1):
# 		for j in range(i+1,len(li)):
# 			if li[i] > li[j]:
# 				li[i],li[j] = li[j],li[i]
# 	return li


"""
1.冒泡排序: 
	每次循环选出最大的放在后面，
	外层循环控制轮数，内层控制每轮的次数(每过一轮减一次)
"""
def bubble_sort(arr):
	"""冒泡排序"""
	for i in range(len(arr)-1):
		for j in range(len(arr)-1-i):
			if arr[j] > arr[j+1]:
				arr[j], arr[j+1] = arr[j+1], arr[j]


def bubble_sort2(arr):
	"""冒泡排序优化:
	若某一轮循环中没有任何元素位置交换，则序列已经排好了序，无需继续，直接跳出；
	"""
	for i in range(len(arr)-1):
		count = 0
		for j in range(len(arr)-1-i):
			if arr[j] > arr[j+1]:
				arr[j], arr[j+1] = arr[j+1], arr[j]
				count += 1
		if count == 0:  # 该轮循环没有任何位置交换
			return

# bubble_sort(arr)
# bubble_sort2(arr)
# print(arr)



"""
2.插入排序 
	1.从第一个元素开始，该元素可以认为已经被排序
	2.取出下一个元素，在已经排序的元素序列中从后向前扫描
	3.如果被扫描的元素（已排序）大于新元素，将该元素后移一位
	4.重复步骤3，直到找到已排序的元素小于或者等于新元素的位置
	5.将新元素插入到该位置后
	6.重复步骤2~5
"""
def insert_sort(arr):
	"""插入排序c"""
	for i in range(1, len(arr)):  # 默认第一个数已经排好序,取第二个数进行插入排序
		while arr[i] < arr[i-1] and i > 0:  # 待插入的数和前面已排好序的数, 从后往前逐个比较,
			arr[i], arr[i-1] = arr[i-1], arr[i]  # 如果待插入的数比前面的数小, 就将两数交换位置, 否则退出while循环; 一直重复该步骤,直到大于前面的数,或i=1,退出循环
			i -= 1

# insert_sort(arr)
# print(arr)


"""
3.快速排序

"""
