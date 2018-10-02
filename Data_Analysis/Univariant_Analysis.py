# -*- coding: utf-8 -*-
import numpy as np
import pandas as pd
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
    df=pd.read_csv("./Data/HR.csv")
    print(df.columns.values.tolist())
    df=df.dropna(axis=0,how="any")
    s_l=df["satisfaction_level"]
    l_e=df["last_evaluation"]
    n_p=df['number_project']
    a_m_h=df['average_monthly_hours']
    t_s_c=df['time_spend_company']
    w_a=df['Work_accident']
    left=df["left"]
    p_l_5=df['promotion_last_5years']
    depart=df['department']
    salary=df['salary']

    # satisfaction level
    print(s_l.describe())
    print(s_l.skew())
    print(s_l.kurt())
    print(np.histogram(s_l,bins=np.arange(0.0,1.0,0.1)))

    # Last Evaluation
    print(l_e.describe())
    print(l_e.skew(),l_e.kurt())
    print(np.histogram(l_e,bins=np.arange(0.0,1.0,0.1)))

    # Number Project
    print(n_p.describe())
    print(n_p.std())
    print(n_p.skew(), n_p.kurt())
    print(n_p.value_counts(normalize=True))

    # Average Monthly Hours
    print(a_m_h.describe())
    print(a_m_h.std())
    print(a_m_h.skew(), a_m_h.kurt())
    print(np.histogram(a_m_h,bins=np.arange(a_m_h.min(),a_m_h.max()+10,10)))

    #Time Spend Company
    print(t_s_c.describe())
    print(t_s_c.std())
    print(t_s_c.skew(), t_s_c.kurt())
    print(t_s_c.value_counts(normalize=True))

    # Work Accident
    print(w_a.describe())
    print(w_a.std())
    print(w_a.skew(), w_a.kurt())
    print(w_a.value_counts(normalize=True))

    # Left
    # print(left)
    print(left.describe())
    print(left.std())
    print(left.skew(), left.kurt())
    print(left.value_counts(normalize=True))

    # Promotion Last 5 Years
    # print(p_l_5)
    print(p_l_5.describe())
    print(p_l_5.std())
    print(p_l_5.skew(), p_l_5.kurt())
    print(p_l_5.value_counts(normalize=True))

    # Department
    print(depart.describe())
    depart= depart.where(depart != "sale").dropna()
    print(depart.value_counts(normalize=True))
    # print(depart)

    # Salary
    print(salary.describe())
    salary=salary.where(salary!="nme").dropna()
    print(salary.value_counts(normalize=True))
    # print(salary)

    #对比分析
    df=df.dropna()
    df=df[df["last_evaluation"]<=1][df["department"]!="sale"][df["salary"]!="nme"]
    print(len(df),df.head(5))
    df1 = df.groupby("department").mean()
    print(df1)
    df2 = df.loc[:,["salary","department"]].groupby(["department","salary"])["salary"].count() # loc 用于切片
    print(df2)
    df3 = df.loc[:,["average_monthly_hours","department"]].groupby("department")["average_monthly_hours"].apply(lambda x:x.max()-x.min())
    print(df3) #极差





if __name__ == '__main__':
    main()