# -*- coding: utf-8 -*-
import numpy as np
from scipy.integrate import quad,dblquad,nquad
from scipy.optimize import minimize
"""
 -------------------------------------------------------------------
    File Name:
    Description:
    Author: Yuxiang Chen
    Date:
 -------------------------------------------------------------------
    Change Activity:
    
 -------------------------------------------------------------------
 """
__author__ = 'Yuxiang Chen'

def main():
    ## 1--Integral
    print(quad(lambda x:np.exp(-x),0,np.inf)) #返回积分制和误差值
    print(dblquad(lambda t,x:np.exp(-x*t)/t**3,0,np.inf, lambda x:1, lambda x:np.inf))
    # dlbquad表示二元积分，t的取值范围用常熟定义，而x的取值范围则实际为t的函数，因此用lambda定义
    def f(x,y):
        return x*y
    def bound_y():
        return [0,0.5]
    def bound_x(y):
        return [0,1-2*y]
    print(nquad(f,[bound_x,bound_y]))


    ## 2-- Optimizer 优化器
    # A. 求函数最小值
    def rosen(x):
        return sum(100.0*(x[1:]-x[:-1]**2.0)**2.0+(1-x[:-1])**2.0)

    x0=np.array([1.3,0.7,0.8,1.9,1.2])
    res=minimize(rosen,x0,method="nelder-mead",options={"xtol":1e-8,"disp":True})
    print("ROSE MINI:",res.x)

    # B. 求目标函数在约定条件下的最小值
    def func(x):
        return (2*x[0]*x[1]+2*x[0]-x[0]**2-2*x[1]**2)

    def func_deriv(x):
        dfdx0=(-2*x[0]+2*x[1]+2) #针对x[0]的导数
        dfdx1=(2*x[0]-4*x[1])    #针对x[1]的导数
        return np.array([dfdx0, dfdx1])
    cons=({'type':'eq',
           'fun':lambda x:np.array([x[0]**3-x[1]]),
           'jac':lambda x:np.array([3.0*(x[0]**2.0),-1.0])},
          {'type':'ineq',
           'fun':lambda x:np.array([x[1]-1]),
           'jac': lambda x:np.array([0.0,1.0])})
    #定义约束条件，jac给出偏导数，比计算机算快。
    res=minimize(func,np.array([-1.0,1.0]),jac=func_deriv,constraints=cons,method='SLSQP',options={'disp':True})
    print("RESTRICT", res)


if __name__ == '__main__':
    main()