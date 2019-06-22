import numpy as np

array = np.array([[1,2,3],
                  [4,5,6],
                  [[4,7],[7,8],[5,4]]])
print(array)
print(array.ndim) #判断几维数组的方法便是看中括号的位置对数有关
print(array.shape)
print(array.size) #元素的个数