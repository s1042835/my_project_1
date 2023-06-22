# -*- coding: utf-8 -*-
"""
Created on Sat May 20 23:25:44 2023

@author: ZHONG SHIH-YING
"""

#*********************************************************************************
import random



class Gchar:
    power = 500
    攻擊力 = 200
    
    def __init__(self, name):       
        self.name = name
       
    
    def active(self,姿勢):
        if 姿勢 == 1:
            print(f"{self.name}使用69大魔王姿勢")
            return 0.5
        
        elif 姿勢 == 2 :  
            print(f"{self.name}使用傳教士插法")
            return random.choice([0,1])
        

class warrior(Gchar):
    
    def attack(self, 姿勢):
        if 姿勢 == 1:
            print(f"{self.name}使用狗喝水")
            return 250
        
        elif 姿勢 == 2:
            print(f"{self.name}使用盤腿抽插")
            return 200

class monster(Gchar):
    
    def attack(self, 姿勢):
        if 姿勢 == 1:
            print(f"{self.name}使用吸精大法")
            return random.choice([200,250])
        
        elif 姿勢 == 2:
            print(f"{self.name}使用奶子攻擊")
            return 200

#*********************************************************************************


































         