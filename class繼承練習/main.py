# -*- coding: utf-8 -*-
"""
Created on Sat May 20 23:25:16 2023

@author: ZHONG SHIH-YING
"""

import random
""" 
from  module import *
your_name = input("選擇名子 : ")
you = warrior(your_name)
girl = monster("桃乃木香奈")
"""
import module
your_name = input("選擇名子 : ")
you = module.warrior(your_name)
girl = module.monster("桃乃木香奈")


隨機 = random.choice([1,2])

while True:
    
    攻擊指令 = int(input("請選擇姿勢(1)狗喝水(2)歡喜佛："))
    攻擊力 = you.attack(攻擊指令)
    失血 = int(girl.active(隨機) * 攻擊力)
    girl.power -= 失血
    
    if girl.power <= 0:
        print(f"{you.name}成功用棒棒征服了{girl.name}")
        break
    else:
        print(f"{girl.name}消耗體力{失血}!距離高潮還有{girl.power}")
        print("--------------------------------")
        
        
    防禦指令 = int(input("請選擇防禦姿勢(1)69(2)傳教士："))
    敵人攻擊力 = girl.attack(攻擊指令)
    失血 = int(you.active(隨機) * 攻擊力)
    you.power -= 失血
    
    if you.power <= 0:
        print(f"{girl.name}成功用鮑魚征服了{you.name}")
        break
    else:
        print(f"{you.name}消耗體力{失血}!距離高潮還有{you.power}")
        print("--------------------------------1")