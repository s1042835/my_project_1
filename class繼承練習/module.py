# -*- coding: utf-8 -*-
"""
Created on Sat May 20 23:25:44 2023
@author: ZHONG SHIH-YING
"""
#*********************************************************************************
import random

class 遊戲角色:
    生命值 = 400
    def __init__(self, 姓名):
        self.姓名 = 姓名
    def 防禦(self, 指令):
        if 指令 == 1:
            print(f"{self.姓名}擺出了格擋姿勢 ~")
            return 0.5
        elif 指令 == 2:
            print(f"{self.姓名}嘗試閃避攻擊 ~")
            return random.choice([0.3, 1])
        

class 戰士(遊戲角色):
    def 攻擊(self, 指令):
        if 指令 == 1:
            print(f"{self.姓名}使出了突刺攻擊！！")
            return 200
        elif 指令 == 2:
            print(f"{self.姓名}奮力使出了迴旋揮砍！！")
            return random.choice([300, 100])
        
        
class 魔物(遊戲角色):
    def 攻擊(self, 指令):
        if 指令 == 1:
            print(f"{self.姓名}使出了利爪攻擊！！")
            return 180
        elif 指令 == 2:
            print(f"{self.姓名}張出血口噴出了毒液！！")
            return random.choice([320, 100])
#*********************************************************************************


































         