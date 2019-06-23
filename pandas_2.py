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