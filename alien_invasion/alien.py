import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
	"""表示单个外星人的类"""


	def __init__(self, ai_game):
		"""初始化外星人"""
		super().__init__()
		self.screen=ai_game.screen
		self.settings=ai_game.settings

		# 加载外星人并设置其rect的属性
		self.image=pygame.image.load('E:/python-basic-project/alien_invasion/images/alien.bmp')
		self.rect=self.image.get_rect()

		# 外星人的初位置在屏幕左上角
		self.rect.x=self.rect.width
		self.rect.y=self.rect.height

		# 存储外星人的精确水平位置
		self.x=float(self.rect.x)


	def check_edges(self):
		screen_rect=self.screen.get_rect()
		if self.rect.right>=screen_rect.right or self.rect.left<=0:
			return True


	def update(self):
		"""使外星人向左或向右移动"""
		self.x+=(self.settings.alien_speed*self.settings.fleet_direction)
		self.rect.x=self.x


	

		
		