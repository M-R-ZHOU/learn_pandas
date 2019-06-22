import numpy as np

array = np.array([[1,2,3],
                  [4,5,6],
                  [7,8,9]],dtype='int64')
print(array)
print(array.ndim) #判断几维数组的方法便是看中括号的位置对数有关
print(array.shape)
print(array.size) #元素的个数
print(array.dtype)#元素的数据类型 整型默认为int32