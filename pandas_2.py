import numpy as np
import pandas as pd

dates = pd.date_range('2019-06-23',periods=6)

df = pd.DataFrame(np.random.randn(6,4),index=dates,columns=['a','b','c','d'])
df2 = pd.DataFrame({'A':1,
                    'B':pd.Timestamp('20190624'),
                    'C':pd.Series(1,index=list(range(4))),
                    'D':np.array([4]*4,dtype='int32'),
                    'E':pd.Categorical(['heh','haha','hehe','heihei']),
                    'F':'pwd'
                    })
print(df2)
print(df2.dtypes)
print(df2.index)
print(df2.columns)
print(df2.values)
print(df2.describe()) #对于混合数据类型，默认只对数值数据进行分析
print(df2.sort_index(axis=1,ascending=False))
print(df2.sort_index(axis=0,ascending=False))
print(df2.sort_values(by='E'))

#选择数据
dates_1  = pd.date_range('20190731',periods=5)
df3 = pd.DataFrame(np.arange(25).reshape((5,5)),index=dates_1,columns=['A','B','C','D','E'])
print(df3)
print('*'*50)
print(df3['A'])#选择一列数据的方式，类似于字典的索引 类似的方式有df3.A
print(df3[::-1]) #类似于列表的索引 但是不可以索引一个数，要切片
#比如要索引第一行必须是[0:1]
print(df3['20190802':'20190804':2])
#另一种对行的操作，类似于上面的方法，但是左右都是闭区间

#select by label : loc
print(df3.loc['20190802',['A','D']])
#该种方法只可以选择一行，对于选定行的列则可以在list里面进行随意选择
#select by position: iloc
print(df3.iloc[[1,2,3],[1,2,3]])
print(df3.iloc[1:4:1,1:4:1])
#该种方法的选择则对于行于列的选取都具有较大的灵活性

#boolean index
print(df3[df3.C>11])
#比较选定的数据，但是其他未比较的数据一并显示
