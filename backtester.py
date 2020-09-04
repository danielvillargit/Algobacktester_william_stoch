# -*- coding: utf-8 -*-
"""
Created on Thu Sep  3 00:28:09 2020

Algo Backtester

Returns
Max drawdown
Max continuous drawdown
Max profit
Max continuous profit
Number of transactions
Average returns per transaction
Transaction charges
Slippages,etc.
Few more points to focus are:

Stop loss/Trailing stop loss
Target price
Entry Criteria
Exit criteria




@author: Daniel Vi
"""

import pandas as pd
import matplotlib.pyplot as plt
from datetime import *
from dateutil.relativedelta import relativedelta
import math

class Backtester:
    
    def __init__(self):
        print("Hello, am backtest Daddy")
        
        
    
    def Stats(self):
        
        self.mean_global = self.df['Price'].cumsum() / len(self.df['Price'])
        self.mean_global = float(self.mean_global.iloc[-1])
        self.max = max(self.df['Price'])
        self.min = min(self.df['Price'])
        sum_var = 0
        for i in c.df['Price']:
            sum_var += (i - self.mean) ** 2
        
        self.std_dev_global = math.sqrt(sum_var/len(self.df['Price']))
        self.variance_global = self.std_dev_global ** 2
        print(self.std_dev)
        print(self.mean_global)
        
    def importText(self):
        #import and cleanup
        self.r = pd.read_csv(r"C:\Users\Daniel\.spyder-py3\backtester\IVE_tickbidask.txt",header=None)
        self.df = pd.DataFrame(self.r)
        self.df.columns = ['Date','Time','Price','Bid','Ask','Size']
        self.df = self.df[self.df['Price'] > 25 ]
        
        self.df['Date'] = pd.to_datetime(self.df['Date'], format = '%m/%d/%Y')
        
    def Sharpe(self):
        self.year_ = []
        self.beg_date = self.df['Date'].iloc[0]
        self.end_date = self.df['Date'].iloc[-1]
        
        tdelta = self.end_date - self.beg_date
        t=0
        while t < tdelta:
            if t==0:
                self.year_.append(self.beg_date)
            else:
                change_ =self.beg_date + relativedelta(years=1)
                self.year_.append(change_)
            t = t + (self.end_date - change_)
        #self.r = relativedelta(years = self.end_date.year - self.beg_date.year) 
        
        #print(self.beg_date)
        #print(self.end_date)
        self.rep_ = str(self.beg_date)
        self.rep_ = self.rep_[0:10]
    
        while self.df[self.df['Date' == self.rep_]]:
           self.year_.append(self.rep_)
           self.rep_.replace(year = self.rep_ + 1)
           print(self.rep_)
          
        
        print(self.df[self.df['Date'] == self.beg_date.replace(year = self.beg_date.year + 1) ].iloc[0,2])
        
    def Plotdata(self):
        x_ = self.df.index
        y_ = [0,x_[-1]]
        plt.plot(x_[y_[0]:y_[1]],self.df['Price'].iloc[y_[0]:y_[1]])



if __name__ == "__main__":
    c = AlgoBackTest()
    c.importText()
    c.Stats()
    