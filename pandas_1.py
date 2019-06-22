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
a = np.arange(0,1,0.01)
b = np.linspace(0,1,101)
c = np.arange(12).reshape((3,4))
#For example, ``a.reshape(10, 11)`` is equivalent to ``a.reshape((10, 11))``.
