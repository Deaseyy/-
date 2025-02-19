# from timeit import Timer

# def t6():
# 	li = []
# 	for i in range(10000):
# 		li.append(i)


# def t7():
# 	li = []
# 	for i in range(10000):
# 		li.insert(0,i)


# s1 = Timer("t6","from __main__ import t6")
# s2 = Timer("t7","from __main__ import t7")

# print(s1.)
# print(s2)



li = [11,22,33,44]
print(id(li))
print(id(li[0]))
print(id(li[1]))
print(id(li[2]))
print(id(li[3]))

# li = [1,2,3,[10,20],6,5,4]
# print(li)
# # print(id(li))
# # print(id(li[2:4]))
# # print(id(li[1]))
# # print(id(li[2]))
# # print(id(li[0:4]))
# # print(id(li[1:3]))
# # li[2]=55
# lii = li[2:4]
# lii.append(100)
# print(lii)
# # lii=(55,66,88)
# # li[2:4]=(55,66,88)
# print(li)

