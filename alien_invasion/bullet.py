import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
	"""管理子弹的类"""


	def __init__(self,ai_game):
		"""在当前位置创建第一个子弹"""
		super().__init__()
		self.screen=ai_game.screen
		self.settings=ai_game.settings
		self.color=self.settings.bullet_color

		# 在(0,0)处创建一个矩形，并设置其位置
		self.rect=pygame.Rect(0,0,self.settings.bullet_width,
			self.settings.bullet_height)
		self.rect.midtop=ai_game.ship.rect.midtop

		# 存储表示子弹位置的小数
		self.y=float(self.rect.y)


	def update(self):
		"""向上移动子弹"""
		# 对表示子弹位置的小数值进行更新
		self.y-=self.settings.bullet_speed
		# 对子弹的rect的位置进行更新
		self.rect.y=self.y


	def draw_bullet(self):
		"""在屏幕上绘制子弹"""
		pygame.draw.rect(self.screen,self.color,self.rect)