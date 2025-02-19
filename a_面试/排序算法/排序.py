print()
'''
冒泡排序  每轮依次拿相邻两个数比较,每轮选出最大(最小)的放在后面; 每轮的比较次数比上一轮少一次
'''
a = [7,5,6,2,8,4,5,6,1,9]
for i in range(len(a)-1): #控制比较轮次
    for j in range(len(a)-1-i): #控制每轮比较次数
        if a[j] > a[j+1]:
            a[j],a[j+1] = a[j+1],a[j]
print(a)


'''
选择排序: 每轮比较, 取该轮第一个数为最小值min, 和后面数进行比较, min总是指向最小的数, 
每轮结束,将该轮最小数放到该轮第一的位置(需交换位置); 
以此类推,每轮找出的最小数不再加入比较, 每轮第一个数的下标比上一轮加1.
'''
a = [7,5,6,2,8,4,5,6,1,9,1,6,4,8]
for i in range(len(a)-1): #轮次

    min = i  #定义最小的数的下标min,假定第一个数最小;
    for j in range(i+1,len(a)):  #找出最小数下标,将该下标上的数放在已经排好序的元素后
        if a[j] < a[min]:
            min = j   # 使min指向最小值的下标
    a[i],a[min] = a[min],a[i]  #将最小的数放在本轮第一个位置

print(a)


'''
快速排序
'''
b = [7,5,6,2,8,6,5,6,1,9,10]
def quick_sorted(b):
    if len(b)<2:
        return b
    index = len(b)//2
    n = b.pop(index) #随便选定一个数弹出来
    left_li = []
    right_li = []
    for i in b:  # 小于n的数放左边， 大于n的放右边
        left_li.append(i) if i<n else right_li.append(i)
    return quick_sorted(left_li)+[n]+quick_sorted(right_li)

res = quick_sorted(b)
print(res)


'''
插入排序c  
1.从第一个元素开始，该元素可以认为已经被排序
2.取出下一个元素，在已经排序的元素序列中从后向前扫描
3.如果被扫描的元素（已排序）大于新元素，将该元素后移一位
4.重复步骤3，直到找到已排序的元素小于或者等于新元素的位置
5.将新元素插入到该位置后
6.重复步骤2~5
'''
li = [6,5,9,4,8,5,2,3,4,0]

for i in range(1, len(li)):          # 默认第一个数已经排好序,取第二个数进行插入排序
    while i > 0 and li[i] < li[i-1]:    # 待插入的数和前面已排好序的数, 从后往前逐个比较,
        li[i], li[i-1] = li[i-1], li[i]  # 如果待插入的数比前面的数小, 就将两数交换位置, 否则退出while循环; 一直重复该步骤,直到大于前面的数,或i=1,退出循环
        i -= 1

print(li)




#  ------------  高阶函数 -----------
print()
'''
#map(f,iter) 将返回一个迭代器   f有且只能有一个参数
'''
a = [2,7,4,5,6,8]
b = range(10)

print(list(map(lambda x:x*x,a)))


'''
reversed(iter) 将iter倒叙,返回一个可迭代对象
'''
a = [2,7,4,5,6,8]

print(list(reversed(a)))
a.reverse()
print(a)


'''
reduce(fun,iter) 把每次结果和序列的下一个元素累计运算,再返回最终结果 有且只有两个参数
'''
from functools import reduce
a = [2,7,4,5,6,8]
print(reduce(lambda x,y:x+y,a))


'''
filter(fun,iter)  将iter中元素一一作用于fun,返回一个函数返回值为真的元素的迭代器
'''
a = [2,7,4,5,6,8]
print(list(filter(lambda x:x>5,b)))


'''
sorted(iter,key,reverse)  将序列中的元素依次作用于key对应的函数,根据作用后的结果将序列中元素按指定reverse排序
'''
a = [2,7,4,5,6,8]

print(sorted(a,key=lambda x:x if x%2==0 else x*x))

'''
zip(iter1,iter2,....)  将iter1,iter2....中并排的元素组成一个元组,以迭代器形式返回
'''