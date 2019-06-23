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
#矩阵的转置的两种方法 np.transpose p.T
mat2 = np.array([1,2,3,4])
m = mat2.transpose()
n = mat2.T
print(m)
a = np.arange(10)
print(np.clip(a, 1, 8,out=a)) 
#out参数表明a数组被返回的结果取代 clip函数的作用是将原有数组值的范围限定在给定的两个参数之间






