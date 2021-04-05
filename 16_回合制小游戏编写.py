#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2020/11/16 16:39 
# @Author : TETE
# @File : 16_回合制小游戏编写.py
'''
1）一个回合制游戏，每个角色都有hp 和power ，hp代表血量，power代表攻击力，hp的初始值为1000，power 的初始值为200.
2）定义一个fight 方法：
final_hp = hp - enemy_power
enemy_final_hp = enemy_hp - power
两个hp 进行对比，血量剩余多的人获胜
'''

# 1.定义game 类
# class Game:
#     def __init__(self,hp,power):
#         self.hp =hp
#         self.power = power
#
#     def fight(self,enemy_hp,enemy_power):
#         final_hp = self.hp - enemy_power
#         enemy_final_hp = enemy_hp - self.power
#         if final_hp > enemy_final_hp:
#             print("我赢了")
#         elif final_hp < enemy_final_hp:
#             print("对方赢了")
#         else:
#             print("平局")
#
# 对hp 和power 进行初始化定义
# hp = 1000
# power = 200
#
# #实例化类
# game = Game(hp,power)
# #调用方法
# game.fight(3000,400)

'''
2.在上一游戏中增加后裔角色，他叫后裔，后裔继承了角色的hp和power ，并多了护甲属性。
houyi_hp = hp +defense-enemy_power
'''

# class Game:
#     def __init__(self,hp,power):
#
#         self.hp =hp
#         self.power = power
#
# class HouYi(Game):
#     def __init__(self):
#         super().__init__(1000,200)
#         self.defense = 100
#
#     def houyi_fight(self,enemy_hp,enemy_power):
#         final_hp = self.hp +self.defense - enemy_power
#         enemy_final_hp = enemy_hp - self.power
#         if final_hp > enemy_final_hp:
#             print("我赢了")
#         elif final_hp < enemy_final_hp:
#             print("对方赢了")
#         else:
#             print("平局")
#
#
# 实例化类
# houyi = HouYi()
#
# 调用方法
# houyi.houyi_fight(200,100)

'''
3.代码优化2：
1）加入模块的改造：
将类houyi 与类角色通过两个文件夹的文件管理
'''



'''
2）加入异常的改造：
当平局时，抛出一个异常
'''


