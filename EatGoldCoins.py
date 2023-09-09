import os
import configparser
import sys
import pygame
import random

'''游戏初始化'''

def initGame():
    #初始化pygame,设置展示窗口
    pygame.init()
    screen=pygame.display.set_mode(configparser.SCREENSIZE)
    pygame.display.set_caption('catch coins —— 九歌')