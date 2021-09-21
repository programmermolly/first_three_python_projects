import pygame
from pygame.sprite import Sprite

class Ship(Sprite):
	"""管理飞船"""
	def __init__(self,ai_game):
		"""初始化飞船"""
		super().__init__()
		self.screen=ai_game.screen
		self.screen_rect=ai_game.screen.get_rect()
		self.settings=ai_game.settings

		# 加载飞船，并获取其外接矩形
		self.image=pygame.image.load('E:/python-basic-project/alien_invasion/images/ship.bmp')
		self.rect=self.image.get_rect()

		# 新飞船的位置在屏幕底部中央
		self.rect.midbottom=self.screen_rect.midbottom

		# 在飞船的x属性中存储小数值
		self.x=float(self.rect.x)

		# 移动标志
		self.moving_right=False
		self.moving_left=False


	def update(self):
		"""调整飞船位置"""
		# 更新飞船的x值
		if self.moving_right and self.rect.right<self.screen_rect.right:
			self.x+=self.settings.ship_speed
		if self.moving_left and self.rect.left>0:
			self.x-=self.settings.ship_speed

		# 根据上述x更新rect对象
		self.rect.x=self.x

	def blitme(self):
		"""在指定位置绘制飞船"""
		self.screen.blit(self.image,self.rect)


	def center_ship(self):
		"""初始化飞船位置"""
		self.rect.midbottom=self.screen_rect.midbottom
		self.x=float(self.rect.x)
