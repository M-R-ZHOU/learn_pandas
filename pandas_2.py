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
#比较选定的数据，但是其他未比较的数据一并显示,同一行同进退

#setting value

df3.iloc[2,2] = 100
print(df3)
df3.loc['20190802',['A','D']] = 200
print(df3)
#df3[df3.A>10] =0
df3.A[df3.A>10] = 0
print(df3)
df3['F'] = np.nan
df3['G'] = np.arange(5)
print(df3)

dates_2  = pd.date_range('20190731',periods=5)
df4 = pd.DataFrame(np.arange(25).reshape((5,5)),index=dates_2,
                   columns=['A','B','C','D','E'])
df4.iloc[3,4] = np.nan
print(df4)
print(df4.dropna(axis=0,how='any'))
print(df4.fillna(value=0))
print(np.any(pd.isna(df4)) == True)

#concatenate
df_1 = pd.DataFrame(np.ones((3,4)),columns=['a','b','c','d'])
df_2 = pd.DataFrame(np.ones((3,4))*0,columns=['a','b','c','d'])
df_3 = pd.DataFrame(np.ones((3,4))*2,columns=['a','b','c','d'])
df_res = pd.concat([df_1,df_2,df_3],axis=0,ignore_index=True)
#ignore_index通过该参数的设定可以忽略掉之前各自的索引，采取新的索引
print(df_res)

df_4 = pd.DataFrame(np.ones((3,5))*0,columns=['a','b','c','d','e'],index=[1,2,3])
df_5 = pd.DataFrame(np.ones((3,3))*2,columns=['b','c','d'],index=[2,3,4])
df_res = pd.concat([df_4,df_5],join='outer',ignore_index=True,sort=True)
# inner outer 参数分别代表交集并集，与sql类似
print(df_res)
df_res = pd.concat([df_4,df_5],axis=1,join_axes=[df_5.index])
#左右相连
print(df_res)
df_6  = pd.DataFrame(np.arange(20).reshape((5,4)),columns=list('ABCD'))
df_7  = pd.Series([6,6,6],index=list('ABC'))
df_8 = df_6.append(df_7,ignore_index=True)
print(df_8)

left = pd.DataFrame({'key':['K0','K1','K2','K3','k5'],
                     'A':['A0','A1','A2','A3','A4'],
                     'B':['B0','B1','B2','B3','B4']
                    })

right = pd.DataFrame({'key':['K0','K1','K2','K3','K4'],
                     'C':['C0','C1','C2','C3','C4'],
                     'D':['D0','D1','D2','D3','D4']
                    })
print(left)
print(right)

"""
SQL-style merge routines
"""

#how = ['inner','outer','left','right']
res = pd.merge(left,right,on='key',how='left')
#类似于sql连接查询的依靠外键 on 可以赋予多个参数，多个外键
print(res)

df_a = pd.DataFrame({'col1':[0,1,2],'col_left':['a','b','c']},index=['A','B','C'])
df_b = pd.DataFrame({'col1':[1,2,2],'col_right':[2,2,5]},index=['B','C','F'])
res = pd.merge(df_a,df_b,on='col1',how='outer',indicator=True)
print(res)
#merged by index
df_a = pd.DataFrame({'col':[0,1,2],'col_left':['a','b','c']},index=['A','B','C'])
df_b = pd.DataFrame({'col':[1,2,2],'col_right':[2,2,5]},index=['B','C','F'])
res = pd.merge(df_a,df_b,left_index=True,right_index=True,how='outer',indicator='hint',suffixes=['_1','_2'])
print(res)
#suffixes该参数可以区分在原本相同的表格中列名重复的情形
boys = pd.DataFrame({'k':['K0','K1','K2'],'age':[10,15,17]})
girls = pd.DataFrame({'k':['K0','K1','K2'],'age':[11,18,13]})
res = pd.merge(boys,girls,on='k',how='outer',suffixes=['_boys','_girls'])
print(res)