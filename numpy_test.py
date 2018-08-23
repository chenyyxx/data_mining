# -*- encoding: utf-8 -*-
import numpy as np
from numpy.linalg import *
"""
 -------------------------------------------------------------------
    File Name: Numpy Learning
    Description: Learning Numpy's most common usage and 
    basic operations.
    Author: Yuxiang Chen
    Date: 07/29/2018
 -------------------------------------------------------------------
    Change Activity:
    
 -------------------------------------------------------------------
 """
__author__ = 'Yuxiang Chen'

def main():
    lst=[[1,3,5],[2,4,6]]
    print(type(lst))
    np_lst=np.array(lst)
    print(type(np_lst))
    print(type(np.array(lst,dtype=np.float)))
    print(np_lst.shape)
    print(np_lst.ndim)
    print(np_lst.dtype)
    print(np_lst.itemsize)

    # Some Special Arrays
    print(np.zeros([3,5])) #all zeros
    print(np.ones([5,5])) #all ones
    print("Rand:")
    print(np.random.rand(3,3)) #生成一个3x3的随机数矩阵
    print(np.random.rand()) #生成一个随机数
    print("RandInt:")
    print(np.random.randint(1,5,7)) #到5之间生成7个随机数
    print(np.random.randn(2,4)) #标准正态分布
    print("Choice:")
    print(np.random.choice([10,20,30])) #随机选择list中其中一个值返回
    print("Distribute:") #生成数学中的常用分布
    print(np.random.beta(1,10,10)) #从1到10生成10个beta分布。

    # Array Operations
    print(np.arange(1,11).reshape([5,-1])) #矩阵转置
    lst=np.arange(1, 11).reshape([2,5])
    print(lst)
    ## Exp
    print(np.exp(lst))
    ## Exp2
    print(np.exp2(lst))
    ## Log
    print(np.log(lst))
    ## Sin
    print(np.sin(lst))
    ## Sqrt
    print(np.sqrt(lst))
    ## Log
    print(np.log(lst))

    print("Sum:")
    lst1 = np.array([[[1,2,3,4],
                      [4,5,6,7]],
                     [[7,8,9,10],
                      [10,11,12,13]],
                     [[14,15,16,17],
                      [17,18,19,20]]])
    print(lst1.sum(axis=0)) #0表示对最外层数组求和，1表示对中间层数组求和，2表示对最内层数组求和
    lst2 = np.array([1,2,3,4])
    lst3 = np.array([10,20,30,40])
    print("Add:")
    print(lst2+lst3)
    print("Sub:")
    print(lst2-lst3)
    print("Mul:")
    print(lst2*lst3)
    print("Div:")
    print(lst2/lst3)
    print("Square:")
    print(lst2**2)
    print("Dot:")
    print(np.dot(lst2,lst3.reshape([4,-1]))) #向量点乘，无法乘出矩阵（无法outer product）
    print("Concatenate")
    print(np.concatenate((lst2,lst3),axis=0))
    print(np.vstack((lst2,lst3)))
    print(np.hstack((lst2,lst3)))
    print(np.split(lst2,4))
    print(np.copy(lst2))


    ## numpy矩阵操作与线性方程组
    print(np.eye(3))
    lst=np.array([[1,2],
                 [3,4]])
    print("Inv:")
    print(inv(lst))
    print("T:")
    print(lst.transpose())
    print("Det:")
    print(det(lst))
    print("Eigen:")
    print(eig(lst))
    ### 解线性方程组
    y=np.array([[5.],[7.]])
    ##### 加点表示为float形式，而非int。其实用int也成立，会向上把int converts成float
    print(solve(lst,y))

    ##其他应用Others
    print("FFT:")  #信号处理
    print(np.fft.fft(np.array([1,1,1,1,1,1,1,1])))
    print("Coeff:") #皮尔逊相关系数
    print(np.corrcoef([1,0,1],[3,1,2]))
    print("Poly:") #生成多项式
    print(np.poly1d([3,1,3]))

if __name__ == '__main__':
    main()