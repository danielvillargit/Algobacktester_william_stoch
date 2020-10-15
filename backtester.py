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
        print("Backtest instance created")
        
        
    
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
        self.r = pd.read_csv(r"C:\Users\Daniel\.spyder-py3\stock_data\IVE_tickbidask.txt",header=None)
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
        self.df = self.df.append(pd.Series(data=None,index = ['DistDay']),ignore_index = True)
        day_count = 1
        for i in range(len(self.df['Date'])+1):
                       
            if self.df['Date'].iloc[i+1] == self.df['Date'].iloc[i]:
                self.df['DistDay'].iloc[i] = day_count
                self.df['DistDay'].iloc[i+1] = day_count
            else:
                self.df['DistDay'].iloc[i] = day_count
                day_count+= 1
                self.df['DistDay'].iloc[i+1] = day_count
        #This loop takes forever...since it's trying to do for 1 million records
        
        
        
        
        
    def Plotdata(self):
        x_ = self.df.index
        y_ = [0,x_[-1]]
        plt.plot(x_[y_[0]:y_[1]],self.df['Price'].iloc[y_[0]:y_[1]])



if __name__ == "__main__":
    c = Backtester()
    c.importText()
    c.Sharpe()
    c.Plotdata()
    
