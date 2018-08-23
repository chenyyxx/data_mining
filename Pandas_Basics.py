# -*- coding: utf-8 -*-
import numpy as np
import pandas as pd
import datetime
from pylab import *
"""
 -------------------------------------------------------------------
    File Name: Pandas_Basics
    Description: Example Code for Learning Pandas
    Author: Yuxiang Chen
    Date: 2018/08/23
 -------------------------------------------------------------------
    Change Activity:
    
 -------------------------------------------------------------------
 """
__author__ = 'Yuxiang Chen'
def main():
    ## Data Structure
    s=pd.Series([i*2 for i in range(1,11)])
    print(type(s))
    dates = pd.date_range("20170301", periods=8)
    df=pd.DataFrame(np.random.randn(8,5),index=dates,columns=list("ABCDE"))
    print(df)
    # df=pd.DataFrame({"A":1,
    #                  "B":pd.Timestamp("20170301"),
    #                  "C":pd.Series(1, index=list(range(4)),dtype="float32"),
    #                  "D":np.array([3]*4,dtype="float32"),
    #                  "E":pd.Categorical(["Police","Student","Teacher","Doctor"])})
    # print(df)


    ## Basics
    print(df.head(3))  #打印出前几行
    print(df.tail(3))  #打印出后几行
    print(df.index)    #打印出primary key
    print(df.values)   #打印出值
    print(df.T)        #转置
    print(df.sort_values("C"))  #根据C列进行排序
    print(df.sort_index(axis=1,ascending=False))
    # print(df.sort_index(axis=0, ascending=False))
    print(df.describe())    #相当于R里面的sumamry

    ## Select
    # ->通过索引进行选择
    print(df["A"])
    print(type(df['A']))
    print(df[:3])
    print(df["20170301":"20170305"])
    print(df.loc[dates[0]])
    print(df.loc["20170301":"20170304",["B","D"]])
    print(df.at[dates[0],"C"])   # 这里不能填写日期，只能填生成的格式

    # ->通过下标进行选择
    print(df.iloc[1:3,2:4])
    print(df.iloc[1,4])
    print(df.iat[1,4])

    # ->填入条件进行筛选（类似SQL中的where）
    print(df[df.B>0][df.A<0])  #表示and
    print(df[df>0])    #只显示df中>0的数
    print(df[df["E"].isin([1,2])])

    ## Set
    s1=pd.Series(list(range(10,18)),index=pd.date_range("20170301",periods=8))
    df['F']=s1
    print(df)
    df.at[dates[0],"A"]=0
    print(df)
    df.iat[1,1]=1
    df.loc[:,"D"]=np.array([4]*len(df))
    print(df)

    ## Copy
    df2=df.copy()
    df2[df2>0]=-df2
    print(df2)

    ### Missing Data Processing
    df1=df.reindex(index=dates[:4],columns=list("ABCD")+["G"])
    df1.loc[dates[0]:dates[1],"G"]=1
    print(df1)
    print(df1.dropna())
    print(df1.fillna(value=2))

    ### Statistics
    print(df.mean())
    print(df.var())
    s= pd.Series([1,2,4,np.nan,5,7,9,10],index=dates)
    print(s.shift(2)) #向下shift两个，没有则为nan
    print(s.diff())  #和上一项的差值
    print(s.value_counts()) #统计每个项目出现频率
    print(df.apply(np.cumsum)) #累加，每一列逐行累加
    print(df.apply(lambda x:x.max()-x.min())) #每一列的极差

    ### Merge & Reshape
    pieces=[df[:3],df[-3:]]
    print(pd.concat(pieces))
    ## Merge
    left=pd.DataFrame({"key":["x","y"],"value":[1,2]})
    right=pd.DataFrame({"key":["x","z"],"value":[3,4]})
    print("LEFT:",left)
    print("RIGHT:",right)
    print(pd.merge(left,right,on="key",how="left")) #根据key这个key做left join
    print(pd.merge(left, right, on="key", how="inner"))
    print(pd.merge(left, right, on="key", how="outer"))
    df3=pd.DataFrame({"A":["a","b","c","b"],"B":list(range(4))})
    print(df3.groupby("A").sum()) #与sql中groupby差不多
    ##Reshape
    df4=pd.DataFrame({'A':['one','one','two','three']*6,
                      'B':['a','b','c']*8,
                      'C':['foo','foo','foo','bar','bar','bar']*4,
                      'D':np.random.randn(24),
                      'E':np.random.randn(24),
                      'F':[datetime.datetime(2017,i,1) for i in range(1,13)]+
                      [datetime.datetime(2017,i,15) for i in range(1,13)]})
    print(df4)
    print(pd.pivot_table(df4,values="D",index=["A","B"],columns=["C"]))
    # 数据透视表，aggfunc设置聚合方式，默认为mean，更改则为aggfunc=[np.sum,np.mean]

    ### Time Series & Graph & Files
    ## Time Series
    t_exam=pd.date_range("20170301",periods=10,freq="S") #S为妙
    print(t_exam)

    ## Graph
    ts=pd.Series(np.random.randn(1000),index=pd.date_range("20170301",periods=1000))
    #randn returns a saple from the "standard" normal distribution (mean 0 var 1)
    #random.normal takes more parameters for more control
    ts.plot()
    show()

    ## Files
    #write
    print(df1)
    df1.to_csv("./test.csv")
    df1.to_excel("./test.xlsx")
    # Read
    df6=pd.read_csv("./test.csv")
    print(df6)
    df7=pd.read_excel("./test.xlsx","Sheet1")
    print("Excel",df7)



if __name__ == '__main__':
    main()