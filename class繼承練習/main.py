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


玩家姓名 = input("請輸入你的姓名：")
玩家 = 戰士(玩家姓名)
敵方 = 魔物("哥布林")
隨機 = random.choice([1, 2])


while True:
    攻擊指令 = int(input("請輸入您的攻擊指令(1)普通攻擊(2)特殊攻擊："))
    玩家攻擊力 = 玩家.攻擊(攻擊指令)
    損血 = int(敵方.防禦(隨機) * 玩家攻擊力)
    敵方.生命值 -= 損血


    if 敵方.生命值 <= 0:
      print(f"{敵方.姓名}倒下了，{玩家.姓名}勝利！！")
      break
    else:
      print(f"{敵方.姓名}受到了 {損血} 傷害！生命值剩下 {敵方.生命值}")
      print("")

    防禦指令 = int(input("請輸入您的防禦指令(1)格擋(2)閃避："))
    敵方攻擊力 = 敵方.攻擊(隨機)
    損血 = int(玩家.防禦(防禦指令) * 敵方攻擊力)
    玩家.生命值 -= 損血


    if 玩家.生命值 <= 0:
      print(f"{玩家.姓名}受傷過重倒下了，遊戲結束 ~")
      break
    else:
      print(f"{玩家.姓名}受到了 {損血} 傷害！生命值剩下 {玩家.生命值}")
      print("")