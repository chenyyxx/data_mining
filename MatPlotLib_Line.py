# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
"""
 -------------------------------------------------------------------
    File Name: MatPlotLib Learning
    Description:
    Author: Yuxiang Chen
    Date: 08/21/2018
 -------------------------------------------------------------------
    Change Activity:
    
 -------------------------------------------------------------------
 """
__author__ = 'Yuxiang Chen'

def main():
    #Line
    x=np.linspace(-np.pi,np.pi,256,endpoint=True)
    c,s=np.cos(x),np.sin(x)
    plt.figure(1)
    plt.plot(x,c,color="blue",linewidth=1.0,linestyle="--",label="Cos",alpha=0.5)
    plt.plot(x,s,"r*",label="Sin",alpha=0.5,linewidth=0.5)
    plt.title("Cos & Sin Function")
    ax=plt.gca()
    ax.spines["right"].set_color("none")
    ax.spines["top"].set_color("none")
    ax.spines["left"].set_position(("data",0))
    # ax.spines["bottom"].set_position(("axes",0.5))
    ax.spines["bottom"].set_position(("data",0))
    ax.xaxis.set_ticks_position("bottom")
    ax.yaxis.set_ticks_position("left")
    plt.xticks([-np.pi,-np.pi/2,0,np.pi/2,np.pi],
               [r'$-\pi$',r'$-\frac{\pi}{2}$',r'$0$',r'$\frac{\pi}{2}$',r'$\pi$'])
    #使用latex语法
    plt.yticks(np.linspace(-1,1,5,endpoint=True)) #不输入endpoint=，则默认为True
    # print(type(ax.get_yticklabels()))
    for label in ax.get_xticklabels()+ax.get_yticklabels():   #"+"表示and
        label.set_fontsize(12)
        label.set_bbox(dict(facecolor="pink",edgecolor="none",alpha=0.1))
    plt.legend(loc="upper left")   #显示之前指定的label
    plt.grid()
    # plt.axis([-1,1,-0.5,1])   #指定显示范围，前两个参数为x轴范围，后两个参数指定y轴范围
    # plt.fill_between(x,c,s,color="blue",alpha=0.1)  #第一个参数表示横轴，第二三个参数表示y轴区间
    plt.fill_between(x,np.abs(x)<0.5,c,c>0.5,color="purple",alpha=0.25)
    # np.abs(x)<0.5 return 0或1，所以y轴区间为0或1到c之间，01判断取决于x,c>0.5限定作图范围。
    t=1
    # plt.plot([0.5,0.5],[0,np.cos(0.5)])
    plt.plot([t,t],[0,np.cos(t)],"orange",linewidth=3,linestyle="--")
    # 表示plot从(t,0)dao(t,cos(t))之间的直线
    plt.annotate("cos(1)",xy=(t,np.cos(1)),xycoords="data",xytext=(+10,+30),
                 textcoords="offset points",arrowprops=dict(arrowstyle="->",connectionstyle="arc3,rad=.2"))
    """
    1. xy表示annotation的坐标，xycoords表示该坐标所用的coordinate system (data表示与被annotate的object一致).
    2. xytext表示annotation中text的位置(如不specify则在xy位置)，textcoords表示该坐标所用的coordinate system.
    3. arrowprops用于绘制一个指向箭头，以一个dict作为参数，用于设置arrowstyle,connectionstyle (Optional).
    """
    plt.show()

if __name__ == '__main__':
    main()
