# -*- coding: utf-8 -*-
"""
Created on Thu Jun  1 09:11:47 2023

@author: ZHONG SHIH-YING
"""
# =============================================================================
#                                   CTRL+4
# 
# class bmi:
#     
#     def __init__( self, weigth, heigth):
#         
#         self.weigth = weigth
#         self.heigth = heigth
#         
#     
#     def bmi_cal(self,):
#         
#         high_pow = self.weigth / (self.heigth/100)**2
#         
#         return  high_pow
# 
# w = int(input("體重："))
# h = int(input("身高：")) 
# 
# bill = bmi(w, h)
# 
# print(bill.bmi_cal())
#                 
# =============================================================================



# =============================================================================

#                            簡易計算機
# class cal:
#     
#     def __init__(self ,n ,symbol ,m ):
#         self.n = n
#         self.m = m
#         self.symbol = symbol
#     
#     def cal(self):
#         
#         if self.symbol == '+':
#             return self.n + self.m
#         
#         if self.symbol == '-':
#             return self.n - self.m
#         
#         if self.symbol == '*':
#             return self.n * self.m
#         
#         if self.symbol == '/':
#             return self.n // self.m
# 
# n = int(input("N:"))        
# symbol = str(input("運算符號:"))        
# m = int(input("M:"))        
# 
# qq =cal(n, symbol, m)
# 
# print("結果為：",qq.cal())
#         
# =============================================================================
import pandas as pd
d = {}

movie ={'name':['fast & furious', 'john wick', 'transformers IV'],
        'profit':[500000000, 400000000 , 300000000], 
        'star':['Car','Killer','Robot']}


print(pd.DataFrame.from_dict(movie))

