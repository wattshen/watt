#!/usr/bin/env python
#coding: utf-8 
#-*-*-  Author: Wattshen       -*-*-
#-*-*-  Email:34665115@qq.com  -*-*-
#-*-*-  Filename:squish.py  -*-*-
#-*-*-  Date: 2015-03-15 
#Content:

import os, sys, pygame
from pygame.locals import *
import object, config
"""这个模块包括Squish游戏的主要游戏逻辑"""

class State:
	"""
	范型游戏状态类，可以处理事件并在给定的表面上显示自身。
	"""

	def handle(self, event):
		"""
		只处理退出事件的默认事件处理
		"""
		if event.type == QUIT:
			sys.exit()
		if event.type == KEYDOWN and event.key == K_ESCAPE:
			sys.exit()
		
	def firstDisplay(self, screen):
		"""
		用于第一次显示状态，使用背景色填充屏幕
		"""
		screen.fill(config.background_color)
		#记得调用flip让更改可见
		pygame.display.flip()

	def display(self, screen):
		"""
		用于在已经显示过一次状态时显示，默认的行为是什么也不做。
		"""
		pass

class Level(State):
	"""
	游戏等级，用于计算已经落下了多少个秤砣，移动子图形以及其它和游戏逻辑相关的任务
	"""
	def __init__(self,number = 1):
		self.number = number
		#本关内还要落下多少秤砣
		self.remaining = config.weights_per_level

		speed = config.drop_speed
		#为每个大于1的等级增加一个speed_increase
		speed += (self.number-1) * config.speed_increase
		#创建秤砣和香蕉
		self.weight =  objects.Weight(speed)
		self.banana = objects.Banana()
		both = self.weight, self.banana #这里可以有更多的角色
		self.sprites = pygame.sprite.RenderUpdates(both)
	
	def update(self, game):
		'''从前一帧更新游戏状态'''
		#更新所有的子图形
		self.sprites.update()
		#如果香蕉碰到了秤砣，那么游戏切换到GameOver状态
		if self.banana.touches(self.weight):
			game.nextState = GameOver()
		#否则在秤砣落地时将其复位
		#如果本关内的所有秤砣都落下了，则让游戏切换到levelCleared状态
		elif self.weight.landed:
			self.weight.reset()
			self.remaining -= 1
			if self.remaining == 0:
				game.nextState = LevevCleared(self.number)
	
	def display(self, screen):
		'''
		在第一次显示（只清空屏幕）后显示状态。与firstDisplay不同，这个方法使用pagame.display.update对self.sprites.draw提供的、需要更新的矩形列表进行更新
		'''
		screen.fill(config.background_color)
		updates = self.sprites.draw(screen)
		pygame.display.update(updates)

class Paused(State):
	"""
	简单的暂停游戏状态，按下键盘上任意键或者点击鼠标都会结束这个状态
	"""
	
	finished = 0 #用户结束暂停了吗？
	image = None#如果需要图片的话，将这个变量设置为文件名
	text = ''#将它设定为一些提示性文本

	def handle(self, event):
		'''
		通过State进行委托（一般处理退出事件）以及对按键和鼠标点击作出反应来处理事件，如果键被按下或者鼠标被点击，将self.finished设定为真
		'''
		State.handle(self,event)
		if event.type in [MOUSEBUTTONDOWN, KEYDOWN]:
			self.finished = 1
	def update(self, game):
		'''
		更新等级，如果按键被按下或者鼠标被点击，那么告诉游戏切换到下一个由self.nextState()表示的状态，应由子类实现
		'''
		if self.finished:
			game.nextState = self.nextState()
	
	def firstDisplay(self, screen):
		screen.fill(config.background_color)

		font = pygame.font.Font(None, config.font_size)
		
		lines = self.text.strip().splitlines()

		height = len(lines)*font.get_linesize()
		
		center, top = screen.get_rect().center
		top -= height // 2
		
		if self.image:
			image = pygame.image.load(self.image).convert()
			r = image.get_rect()
			
			top += r.height // 2

			r.midbottom = center, top -20
			screen.blit(image, r)
		
		antialias = 1
		black = 0,0,0

		for line in lines:
			text = font.render(line.strip(),antialias,black)
			r = text.get_rect()
			r.midtop = center, top
			screen.blit(text, r)
			top += font.get_linesize()
		pygame.display.flip()

class Info(Paused):
	nextState = Level
	text = '''
	in this game you are a banana,
	trying to do
	'''

class StartUp(Paused):
	nextState = Info
	image = config.splash_image
	text ='''
	Welcome to here
	'''
class LevelCleared(Paused):
	def __init__(self, number):
		self.number = number
		self.text = '''
		Level %i celared 
		Click to start next level''' % self.number

	def nextState(self):
		return Level(self.number+1)

class GameOver(Paused):
	
	nextState = Level
	text = '''
	Gave OVER
	'''

class Game:
	'''
	ok
	'''
	def __init__(self, *args):
		path = os.path.abspath(args[0])
		dir = os.path.split(path)[0]
		os.chdir(dir)
		self.state = None
		self.nextState = StartUp()

	def run(self):
		pygame.init()
		flag = 0
		
		if config.full_screen:
			flag = FULLSCREEN
		screen_size = config.screen_size
		screen = pygame.display.set_mode(screen_size, flag)

		pygame.display.set_caption('fruit Self Defense')
		pygame.mouse.set_visible(False)

		while True:
			if self.state != self.nextState:
				self.state = self.nextState
				self.state.firstDisplay(screen)
			for event in pygame.event.get():
				self.state.handle(event)
		self.state.update(self)
		self.state.display(screen)

if __name__ == '__main__':
	game = Game(*sys.argv)
	game.run()