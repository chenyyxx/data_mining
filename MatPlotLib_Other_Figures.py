# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
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
    ## Scatter
    fig=plt.figure()
    ax=fig.add_subplot(3,3,1)
    n=128
    X=np.random.normal(0,1,n)
    Y=np.random.normal(0,1,n)
    T=np.arctan2(Y,X)   #用于上色
    # plt.axes([0.025,0.025,0.95,0.95])  #指定显示范围
    ax.scatter(X,Y,s=75,c=T,alpha=.5)
    #s表示点的大小，c表示颜色
    plt.xlim(-1.5,1.5), plt.xticks([])
    plt.ylim(-1.5,1.5,), plt.yticks([])
    plt.axis()
    plt.title("scatter")
    plt.xlabel("x")
    plt.ylabel("y")
    # plt.show()

    ##Bar Chart
    fig.add_subplot(3,3,2)
    n=10
    X=np.arange(n) #生成一个1-9的数组
    # np.arange(),一个参数表示数组数目，两个参数表示区间，三个参数表示区间和步长
    Y1=(1-X/float(n))*np.random.uniform(0.5,1.0,n)  #生成一个均匀分布的随机采样
    Y2=(1-X/float(n))*np.random.uniform(0.5,1.0,n)
    plt.bar(X,+Y1, facecolor="#9999ff",edgecolor='white')
    plt.bar(X,-Y2, facecolor="#ff9999",edgecolor='white')
    for x,y in zip(X,Y1):   # zip() 函数用于将可迭代对象作为参数，将对象中对应的元素打包成一个个元组，然后返回由这些元组组成的对象。
        plt.text(x,y+0.05, '%.2f'%y, ha='center',va='bottom')
        # '%.2f'%y 代表格式（保留两位小数点）， ha代表水平位置（horizontal），va代表垂直位置（vertical），va中bottom代表图表在文字下方
    for x,y in zip(X,Y2):
        plt.text(x,-y-0.05,'%.2f'%y, ha='center',va='top')

    ##Pie Chart
    fig.add_subplot(333)
    n=20
    Z=np.ones(n) #定义一个全1的变量
    Z[-1] *= 2
    plt.pie(Z, explode=Z*0.05, colors=['%f'%(i/float(n)) for i in range(n)],
            labels=['%.2f'%(i/float(n)) for i in range(n)])
    # explode 表示每一个扇形离圆心的距离，‘%f’表示设置灰度颜色, 这里面的label打印的是颜色的值
    plt.gca().set_aspect('equal')
    # gca=>Get the current Axes instance on the current figure
    # et_aspect('equal')表示让图标为正圆，而非根据画布大小调整为椭圆
    plt.xticks([]),plt.yticks([])

    ##polar 极值图
    fig.add_subplot(334, polar=True)
    n=20
    theta=np.arange(0.0,2*np.pi,2*np.pi/n)
    radii=10*np.random.rand(n)
    # plt.plot(theta, radii)  #线图 画这个需要polar=False
    plt.polar(theta,radii)    #雷达图

    ##Heat Map
    from matplotlib import cm #给热图上色用的
    fig.add_subplot(335)
    data=np.random.rand(3,3)  #生成一个3X3的随机数矩阵
    cmap=cm.Reds
    map = plt.imshow(data, interpolation='nearest',cmap=cmap,aspect='auto',vmin=0,vmax=1)
    #aspect表示指定缩放, interpolation表示差值方法

    ##3D
    from mpl_toolkits.mplot3d import Axes3D
    ax=fig.add_subplot(336,projection="3d")  #画3D图需要指定projection
    ax.scatter(1,1,3, s=100)

    ##Hot Map 热力图
    fig.add_subplot(313)
    def f(x,y):
        return (1-x/2+x**5+y**3)*np.exp(-x**2-y**2) #定义一个函数
    n=256
    x=np.linspace(-3,3,n)
    y=np.linspace(-3,3,n)
    X,Y=np.meshgrid(x,y)  #必要，生成一个坐标轴（meshgrid函数用两个坐标轴上的点在平面上画格）
    plt.contourf(X,Y,f(X,Y),8,alpha=0.75,cmap=plt.cm.hot)
    # plt.savefig("fig.png")  #保存图像
    plt.show()



if __name__ == '__main__':
    main()