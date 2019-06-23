import numpy as np

array = np.array([[1,2,3],
                  [4,5,6],
                  [7,8,9]],dtype='int64')
print(array)
print(array.ndim) #判断几维数组的方法便是看中括号的位置对数有关
print(array.shape)
print(array.size) #元素的个数
print(array.dtype)#元素的数据类型 整型默认为int32

ones = np.ones((4,5),dtype='int64')
zeros = np.zeros((4,3))
a = np.arange(0,1,0.01) #不包含1，自增大小为第三个参数
b = np.linspace(0,1,101) #包含1 ，自增大小为 （1-0）/（101-1）
c = np.arange(12).reshape((3,4))
#For example, ``a.reshape(10, 11)`` is equivalent to ``a.reshape((10, 11))``.

#numpy的运算
a1 = np.array([[1,2],[3,4]])
b1 = np.arange(4).reshape(2,2)
c1 = a1 + b1
result1 = a1 * b1 #数组对应元素的乘积
result2 = np.dot(a1,b1) #矩阵的乘法

mat = np.random.randint(4,size = (3,3)) #
sum = np.sum(mat)#全体数据求和
sum1 = np.sum(mat,axis=1) #按照行求和
sum2 = np.sum(mat,axis=0) #按照列求和
# np.min np.min 与 np.max 的使用与sum类似
p = np.median(np.array([[4,5],[17,12]])) #输出中位数
#np.cumsum 累和 返回的是每一次累和后的结果
# np.nonzero Return the indices of the elements that are non-zero.
sort = np.sort(np.array([[5,7,1],[45,6,74]]),axis=0)  # 二维数组中 axis = 1 等价于 -1 sort默认为-1
#矩阵的转置的两种方法 np.transpose p.T 对于二维数组 两种方法的结果是相同的
#对于高维度数组 比如三维数组 T == transpose(2,1,0) 
mat2 = np.array([1,2,3,4])
m = mat2.transpose()
n = mat2.T
print(m)
a = np.arange(10)
print(np.clip(a, 1, 8,out=a))
#out参数表明a数组被返回的结果取代 clip函数的作用是将原有数组值的范围限定在给定的两个参数之间

#index 对于一维数组索引类似于list 对于常用的二维数组来说 [1,2]代表第2行第三列 [1,:]代表第二行的全部数据
#与list的切片操作一致
mat3 = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(mat3[1,::2])
# for 循环迭代矩阵的每一行，若想迭代每一行，则可以将矩阵进行转置矩阵，在进行循环迭代
for i in mat3:
    print(i)
#print(mat3.flatten()) #降维至一
#print(mat3.flat)  #类似与迭代器，使其可迭代
#print(np.ones((1,3)))  #[[1. 1. 1.]] 代表二维数组
#print(np.ones((3,)))#[1. 1. 1.]  代表一维数组

# 数组的合并
# vertical stack 竖直堆放 horizontal stack 水平堆放
a_1 = np.array([1,2,3,4])
b_1 = np.arange(10,14)
a_2 = a_1[:,np.newaxis] #添加一个维度，将行向量转变为列向量
b_2 = b_1[:,np.newaxis]
c_2 = np.hstack((a_2,b_2))

print(c_2)
print(np.ones((3,1)))
c_1 = np.vstack((a_1,b_1))
# vstack对于数组的合并更加灵活 两个一维行向量合并可以变成二维的
print(c_1.ndim)
c_3 = np.concatenate((np.array([[1,2,3],[4,5,6]]),np.array([[1,2,3]])),axis=0)
#concatenate 对于数组的合并则要求目标数组维度要一致，同时，
# 当对两个一维行向量进行合并时无法变成二维的，依旧是一维的
print(c_1)
print(c_3)
#数组的分割
mat_1 = np.random.randint(10,size = (5,7))
print(mat_1)
print(np.split(mat_1,[3,4],axis=1))
#split 第二个参数是一个int时，代表等分，若不能等分则会报错 参数也可以指定一个列表
#可以按照自己的意愿进行分割
'''
    Please refer to the ``split`` documentation.  ``vsplit`` is equivalent
    to ``split`` with `axis=0` (default), the array is always split along the
    first axis regardless of the array dimension.
'''


